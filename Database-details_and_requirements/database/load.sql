LOAD DATA INFILE 'C:\xampp\data\buyer.csv'
INTO TABLE buyer_buyer
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n' 
IGNORE 1 ROWS
(id, buyer_name, email, password);

LOAD DATA INFILE 'C:\xampp\data\seller.csv'
INTO TABLE seller_seller
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n' 
IGNORE 1 ROWS
(id, seller_name, email, password);

LOAD DATA INFILE 'C:\xampp\data\authenticate.csv'
INTO TABLE buyer_authentication
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(id, password, buyer_id);

LOAD DATA INFILE 'C:\xampp\data\product.csv'
INTO TABLE products_products
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(id, title, description, price, seller_id);

LOAD DATA INFILE 'C:\xampp\data\payment.csv'
INTO TABLE payment_payment
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(id, amount, payment_date buyer_id, product_id);

LOAD DATA INFILE 'C:\xampp\data\bids.csv'
INTO TABLE products_bid
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(id, buyer_id, product_id);

LOAD DATA INFILE 'C:\xampp\data\listings.csv'
INTO TABLE products_listing
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(id, status, start_date, end_date, seller_id);

