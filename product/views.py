from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user, authenticate, login
from django.contrib.auth.models import User
from django.db.models import Max
from django.core.files.storage import FileSystemStorage
from buyer.models import *
from seller.models import *
from .models import *
from payment.models import *
import datetime
import os

# Create your views here.
def signup(request):
    if request.method == "GET":
        return render(request, "signup.html")
    else:
        person = request.POST.get('user')
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        password = request.POST.get('password')
        re_password = request.POST.get('confirm_password')
        error_msg = None
        if password != re_password:
            error_msg = "Hey! Your Password Not Matched"

        elif User.objects.filter(email=email).first():
            error_msg = "This Username Has Been Already Registered"

        if not error_msg:
            if person == "buyer":
                user_object = User.objects.create(username=None, email=email)
                user_object.set_password(password)
                user_object.save()
                new_user_obj = User.objects.filter(email=email).first()
                buyer_object = Buyer.objects.create(buyer_name=name, email=email, address=address, user_id=new_user_obj.id)
                buyer_object.save()
                new_buyer_object = Buyer.objects.filter(email=email).first()
                auth_object = AuthenticateForBuyer.objects.create(buyer_id=new_buyer_object.id, password=password)
                auth_object.save()
            if person == "seller":
                user_object = User.objects.create(username=None, email=email)
                user_object.set_password(password)
                user_object.save()
                new_user_obj = User.objects.filter(email=email).first()
                seller_object = Seller.objects.create(seller_name=name, email=email, address=address, user_id=new_user_obj.id)
                seller_object.save()
                new_seller_object = Seller.objects.filter(email=email).first()
                auth_object = AuthenticateForSeller.objects.create(seller_id=new_seller_object.id, password=password)
                auth_object.save()

            user = User.objects.filter(email=email).first()
            login(request, user)
            return redirect('home')
        else:
            data = {
                "error": error_msg,
            }
            return render(request, 'signup.html', data)

def signin(request):
    if request.method == "GET":
        return render(request, 'signin.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        person = request.POST.get('user')
        error_msg = ""
        if person == "buyer":
            buyer_object = Buyer.objects.filter(email=email).first()
            # print(buyer_object.id)
            if buyer_object is None:
                error_msg = "User not found. Please try again"
            else:
                authenticate_object = AuthenticateForBuyer.objects.get(buyer_id=buyer_object.id)
                # print(authenticate_object.password)
                if authenticate_object.password == password:
                    user = User.objects.filter(email=email).first()
                    login(request, user)
                    return redirect('home')
                else:
                    error_msg = "Wrong password."
        if person == "seller":
            seller_object = Seller.objects.filter(email=email).first()
            # print(seller_object.id)
            if seller_object is None:
                error_msg = "User not found. Please try again"
            else:
                authenticate_object = AuthenticateForSeller.objects.get(seller_id=seller_object.id)
                # print(authenticate_object.password)
                if authenticate_object.password == password:
                    user = User.objects.filter(email=email).first()
                    login(request, user)
                    return redirect('home')
                else:
                    error_msg = "Wrong password."

        # print(email, password, person)
        data = {
            "error": error_msg,
        }
        return render(request, 'signin.html', data)

@login_required
def home(request):
    user = get_user(request)
    buyer = Buyer.objects.filter(user_id=user.id).first()
    if request.method == "GET":
        available_product = Listings.objects.filter(status="Active")
        array_product = list()
        array_max_bid = list()
        for x in available_product:
            array_product.append(Product.objects.get(id=x.product_id))
        for product in array_product:
            array_max_bid.append({product.id:Bid.objects.filter(product_id=product.id).aggregate(Max('amount'))['amount__max']})
        # print(array_product)
        # print(array_max_bid)
        return render(request, 'home.html', {"data": array_product, "max_bid": array_max_bid, "listing":available_product})
    else:
        bid_amount = request.POST.get('bid')
        product_id = request.POST.get('product_id')
        # print(bid_amount, product_id)
        maximum_amount = Bid.objects.filter(product_id=product_id).aggregate(Max('amount'))['amount__max']
        # print(maximum_amount)
        today = datetime.date.today()
        deadline = Listings.objects.get(product_id = product_id)
        error_msg = None
        if (today <= deadline.end_date):
            if (maximum_amount == None):
                bid_obj = Bid.objects.create(amount=bid_amount, buyer_id=buyer.id, product_id=product_id)
                bid_obj.save()
                return redirect('home')
            elif (float(bid_amount) <= maximum_amount):
                error_msg = "Hey! You need to bid more amount for this product. Please back and bid again"
            else:
                bid_obj = Bid.objects.create(amount=bid_amount, buyer_id=buyer.id, product_id=product_id)
                # print(bid_obj)
                bid_obj.save()
                return redirect('home')
        else:
            error_msg = "Sorry you can't bid because the deadline is over."
        return render(request, 'home_error.html', {"error": error_msg})


@login_required
def profile(request):
    user = get_user(request)
    buyer = Buyer.objects.filter(user_id=user.id).first()
    seller = Seller.objects.filter(user_id=user.id).first()
    
    if buyer is not None:
        if request.method == "GET":
            print(buyer.buyer_name, buyer.email, buyer.address, buyer.profile_pic)
            buyer_biding = Bid.objects.filter(buyer_id=buyer.id)
            buyer_bidding_product_lists = dict()
            for b in buyer_biding:
                x = Product.objects.get(id=b.product_id)
                y = Listings.objects.get(product_id = b.product_id, seller_id = x.seller_id)
                z = None
                if (y.status == "Bought"):
                    z = Payment.objects.get(bid_id=b.id, buyer_id=buyer.id)
                list_dic = dict()
                list_dic.update({"title": x.title})
                list_dic.update({"price": x.price})
                list_dic.update({"end_date": y.end_date})
                list_dic.update({"amount": b.amount})
                if z is not None:
                    list_dic.update({"payment_time": z.payment_time})
                else:
                    list_dic.update({"payment_time": "-"})
                list_dic.update({"status": y.status})
                buyer_bidding_product_lists.update({b.id: list_dic})
            # print(buyer_bidding_product_lists)

            data = {
                'id': buyer.id,
                'name': buyer.buyer_name,
                'email': buyer.email,
                'address': buyer.address,
                'profile_pic': buyer.profile_pic,
                'buyer_biding': buyer_biding,
                'buyer_bidding_product_lists': buyer_bidding_product_lists,
            }
            return render(request, 'buyer_profile.html', data)
        
        if request.method == "POST":
            # image = request.FILES['picture']
            # fs = FileSystemStorage()
            # print(fs, image)
            # fs.save("buyer_picture/"+image.name, image)
            # buyer.profile_pic = "buyer_picture/"+image.name
            # buyer.save()
            # return redirect('profile')
            new_bid_amount = request.POST.get('new-price')
            bid_id = request.POST.get('bid_id')
            # print(new_bid_amount, bid_id, buyer.id)
            bidding_product = Bid.objects.get(id=bid_id, buyer_id=buyer.id)
            bidding_product_in_listing = Listings.objects.get(product_id=bidding_product.product_id)
            # print(bidding_product.id, bidding_product.amount, bidding_product.buyer_id, bidding_product.product_id)
            maximum_amount = Bid.objects.filter(product_id=bidding_product.product_id).aggregate(Max('amount'))['amount__max']
            print(maximum_amount, bidding_product_in_listing.end_date)
            error_msg = None
            today = datetime.date.today()
            if (today <= bidding_product_in_listing.end_date):
                if (float(new_bid_amount) <= maximum_amount):
                    error_msg = "Hey! You need to bid more amount for this product. Please back and bid again"
                else:
                    bidding_product.amount = new_bid_amount
                    bidding_product.save()
                    return redirect('profile')
            else:
                error_msg = "Sorry you can't bid because the deadline is over."
            return render(request, 'buyer_profile_error.html', {"error": error_msg})

    if seller is not None:
        if request.method == "GET":
            seller_products = Product.objects.filter(seller_id=seller.id)
            seller_products_listing = Listings.objects.filter(seller_id=seller.id)
            data = {
                'name': seller.seller_name,
                'email': seller.email,
                'address': seller.address,
                'profile_pic': seller.profile_pic,
                'seller_products': seller_products,
                'seller_products_listing': seller_products_listing,
            }
            return render(request, 'seller_profile.html', data)
        
        else:
            product_name = request.POST.get('product-name')
            description = request.POST.get('description')
            price = request.POST.get('price')
            deadline = request.POST.get('deadline')
            status = request.POST.get('status')
            # image = request.FILES('picture')
            todays_date = datetime.date.today()
            # print(product_name, description, picture, price, todays_date, deadline, status)
            product = Product.objects.create(title=product_name, description=description, price=price, seller_id = seller.id)
            product.save()
            product = Product.objects.get(title=product_name, price=price, seller_id = seller.id)
            listing_product = Listings.objects.create(status=status, start_date=todays_date, end_date=deadline, seller_id = seller.id, product_id=product.id)
            listing_product.save()
            # fs = FileSystemStorage()
            # fs.save(image.name, image)
            return redirect('profile')

