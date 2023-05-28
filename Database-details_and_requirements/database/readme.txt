Task B:
For the given relations SQL code is implemented for its creation and insertion: 
Table 1: Buyer (Buyer_id, Buyer_Name, Email, Address) 

Table creation:

CREATE TABLE Buyer (
  Buyer_id INT NOT NULL PRIMARY KEY,
  Buyer_Name VARCHAR(20) NOT NULL,
  Email VARCHAR(20) NOT NULL,
  Address VARCHAR(20) NOT NULL
);

Inserting value into table:

INSERT INTO Buyer (Buyer_id, Buyer_Name, Email, Address) VALUES 
(1, 'John Doe', 'john.doe@example.com', '123 Main St'),
(2, 'Jane Smith', 'jane.smith@example.com', '456 Oak Ave'),
(3, 'Bob Johnson', 'bob.johnson@example.com', '789 Maple Rd'),
(4, 'Sarah Lee', 'sarah.lee@example.com', '321 Elm Blvd'),
(5, 'Mike Brown', 'mike.brown@example.com', '654 Pine St'),
(6, 'Lisa Davis', 'lisa.davis@example.com', '987 Cedar Ave'),
(7, 'Mark Wilson', 'mark.wilson@example.com', '555 Cherry Ln'),
(8, 'Emily Taylor', 'emily.taylor@example.com', '444 Orange St'),
(9, 'David Clark', 'david.clark@example.com', '777 Grapevine Rd'),
(10, 'Karen Adams', 'karen.adams@example.com', '222 Lemon St');

Table 2: Seller (Seller_id, Seller_Name, Email, Address) 

Table creation:

CREATE TABLE Seller (
  Seller_id INT NOT NULL PRIMARY KEY,
  Seller_Name VARCHAR(20) NOT NULL,
  Email VARCHAR(20) NOT NULL,
  Address VARCHAR(20) NOT NULL
);

Inserting value into table:

INSERT INTO Seller (Seller_id, Seller_Name, Email, Address) VALUES 
       (1, 'ABC Corp', 'abccorp@example.com', '123 Main St'),
       (2, 'XYZ Inc', 'xyzinc@example.com', '456 Oak Ave'),
       (3, 'Smith Co', 'smithco@example.com', '789 Maple Dr'),
       (4, 'Jones Enterprises', 'jonesent@example.com', '321 Pine St'),
       (5, 'Wilson LLC', 'wilsonllc@example.com', '654 Elm St'),
       (6, 'Miller & Sons', 'millerandsons@example.com', '987 Cedar Dr'),
       (7, 'Johnson & Co', 'johnsonandco@example.com', '246 Willow Ave'),
       (8, 'Brown Industries', 'brownind@example.com', '135 Oak St'),
       (9, 'Green Solutions', 'greensol@example.com', '864 Maple Dr'),
       (10, 'Davis Enterprises', 'davisent@example.com', '975 Pine St');

Table 3: Authenticate (Auth_id, Password, Buyer_id) 


Table creation:
CREATE TABLE Authenticate (
  Auth_id INT NOT NULL PRIMARY KEY,
  Password VARCHAR(20) NOT NULL,
  Buyer_id INT NOT NULL,
  FOREIGN KEY (Buyer_id) REFERENCES Buyer(Buyer_id)
);

Inserting value into table:

INSERT INTO Authenticate (Auth_id, Password, Buyer_id) VALUES
       (1, 'password1',1),
       (2, 'password2',2),
       (3, 'password3',3),
       (4, 'password4',4),
       (5, 'password5',5),
       (6, 'password6',6),
       (7, 'password7',7),
       (8, 'password8',8),
       (9, 'password9',9),
       (10, 'password10',10);

Table 4: Product (P_id, Title, Description, Price, Seller_id) 

Table creation:

CREATE TABLE Product (
  P_id INT NOT NULL PRIMARY KEY,
  Title VARCHAR(20) NOT NULL,
  Description VARCHAR(20) NOT NULL,
  Price DECIMAL(10, 2) NOT NULL,
  Seller_id INT NOT NULL,
  FOREIGN KEY (Seller_id) REFERENCES Seller(Seller_id)
);

Inserting value into table:

Insert into Product (P_id, Title, Description, Price, Seller_id) values (1, 'iPhone 12', 'Apple iPhone 12 with 256GB Storage', 1099.99, 1);
Insert into Product (P_id, Title, Description, Price, Seller_id) values (2, 'Samsung Galaxy S21', 'Samsung Galaxy S21 with 128GB Storage', 799.99, 2);
Insert into Product (P_id, Title, Description, Price, Seller_id) values (3, 'Sony Playstation 5', 'Sony Playstation 5 Gaming Console', 499.99, 3);
Insert into Product (P_id, Title, Description, Price, Seller_id) values (4, 'Microsoft Surface Laptop 4', 'Microsoft Surface Laptop 4 with 512GB Storage', 1499.99, 4);
Insert into Product (P_id, Title, Description, Price, Seller_id) values (5, 'Bose QuietComfort Earbuds', 'Bose QuietComfort Earbuds with Noise Cancellation', 279.99, 5);
Insert into Product (P_id, Title, Description, Price, Seller_id) values (6, 'LG OLED TV', 'LG OLED TV with 65 inch Display', 1999.99, 6);
Insert into Product (P_id, Title, Description, Price, Seller_id) values (7, 'Canon EOS R6', 'Canon EOS R6 Full-Frame Mirrorless Camera', 2499.99, 7);
Insert into Product (P_id, Title, Description, Price, Seller_id) values (8, 'DJI Mavic Air 2', 'DJI Mavic Air 2 Drone with 48MP Camera', 799.99, 8);
Insert into Product (P_id, Title, Description, Price, Seller_id) values (9, 'Nest Learning Thermostat', 'Nest Learning Thermostat for Smart Homes', 249.99, 9);
Insert into Product (P_id, Title, Description, Price, Seller_id) values (10, 'Fitbit Sense', 'Fitbit Sense Smartwatch with Health Tracking', 299.99, 10);
Table 5: Payment (Payment_id, Bid_id, B_id, Amount, Payment_time) 

Table creation:

CREATE TABLE Payment (
  Payment_id INT NOT NULL PRIMARY KEY,
  Bid_id INT NOT NULL,
  B_id INT NOT NULL,
  Amount INT NOT NULL,
  Payment_time DATETIME NOT NULL,
  FOREIGN KEY (Bid_id) REFERENCES Bids(Bid_id),
  FOREIGN KEY (B_id) REFERENCES Buyer(Buyer_id)
);

Inserting value into table:

INSERT INTO Payment (Payment_id, Bid_id, B_id, Amount, Payment_time) VALUES
    (11, 10, 4, 100, '2022-02-01 12:00:00'),
    (12, 11, 3, 200, '2022-02-02 13:00:00'),
    (13, 12, 1, 150, '2022-02-03 14:00:00'),
    (14, 13, 3, 300, '2022-02-04 15:00:00'),
    (15, 14, 4, 250, '2022-02-05 16:00:00'),
    (16, 15, 2, 400, '2022-02-06 17:00:00'),
    (17, 16, 1, 500, '2022-02-07 18:00:00'),
    (18, 17, 2, 350, '2022-02-08 19:00:00'),
    (19, 18, 3, 450, '2022-02-09 20:00:00'),
    (20, 19, 4, 550, '2022-02-10 21:00:00');

Table 6: Bids (Bid_id, B_id, P_id) 

Table creation:

CREATE TABLE Bids (
  Bid_id INT NOT NULL PRIMARY KEY,
  B_id INT NOT NULL,
  P_id INT NOT NULL,
  FOREIGN KEY (B_id) REFERENCES Buyer(Buyer_id),
  FOREIGN KEY (P_id) REFERENCES Product(P_id)
);

Inserting value into table:

INSERT INTO Bids (Bid_id, B_id, P_id, Amount) VALUES 
       (1, 3, 1, 150.00),
       (2, 2, 2, 200.00),
       (3, 1, 3, 100.00),
       (4, 4, 1, 175.00),
       (5, 5, 2, 225.00),
       (6, 3, 4, 50.00),
       (7, 2, 3, 125.00),
       (8, 1, 4, 90.00),
       (9, 4, 3, 175.00),
       (10, 5, 1, 200.00);


Table 7: Listings (Listing_id, Seller_id, Status, Start_date, End_date)
Table creation:
CREATE TABLE Listings (
  Listing_id INT NOT NULL PRIMARY KEY,
  Seller_id INT NOT NULL,
  Status VARCHAR(20) NOT NULL,
  Start_date DATE NOT NULL,
  End_date DATE NOT NULL,
  FOREIGN KEY (Seller_id) REFERENCES Seller(Seller_id)
);
Inserting value into table:

INSERT INTO listings (listing_id, seller_id, status, start_date, end_date) VALUES
(1, 1, 'Active', '2022-01-01', '2022-12-31'),
(2, 2, 'Active', '2022-01-01', '2022-12-31'),
(3, 3, 'Active', '2022-01-01', '2022-12-31'),
(4, 4, 'Inactive', '2022-01-01', '2022-06-30'),
(5, 5, 'Inactive', '2022-01-01', '2022-06-30'),
(6, 6, 'Inactive', '2022-01-01', '2022-06-30'),
(7, 7, 'Active', '2022-07-01', '2022-12-31'),
(8, 8, 'Active', '2022-07-01', '2022-12-31'),
(9, 9, 'Active', '2022-07-01', '2022-12-31'),
(10, 10, 'Inactive', '2022-07-01', '2022-12-31');

Source of data:

Data Sources:

1. Buyers.csv - This file contains data for the Buyers table and was sourced imaginary.

2. Sellers.csv - This file contains data for the Sellers table and was sourced imaginary.

3. Authenticate.csv - This file contains data for the Authenticate table and was sourced imaginary.

4. Products.csv - This file contains data for the Products table and was sourced imaginary.

5. Payments.csv - This file contains data for the Payments table and was sourced imaginary.

6. Bids.csv - This file contains data for the Bids table and was sourced imaginary.

7. Listings.csv - This file contains data for the Listings table and was sourced imaginary.
































___________________________________________________________________________
