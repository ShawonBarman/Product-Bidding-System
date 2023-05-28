from django.contrib import admin
from django.urls import path
from buyer import views as buyer_views
from seller import views as seller_views
from product import views as products_views
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', products_views.signin, name="signin"),
    path('singup/', products_views.signup, name="signup"),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('home/', products_views.home, name="home"),
    path('profile/', products_views.profile, name="profile"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
