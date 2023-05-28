CREATE TABLE Buyer (
  Buyer_id INT NOT NULL PRIMARY KEY,
  Buyer_Name VARCHAR(20) NOT NULL,
  Email VARCHAR(20) NOT NULL,
  Address VARCHAR(20) NOT NULL
);

CREATE TABLE Seller (
  Seller_id INT NOT NULL PRIMARY KEY,
  Seller_Name VARCHAR(20) NOT NULL,
  Email VARCHAR(20) NOT NULL,
  Address VARCHAR(20) NOT NULL
);

CREATE TABLE Authenticate (
  Auth_id INT NOT NULL PRIMARY KEY,
  Password VARCHAR(20) NOT NULL,
  Buyer_id INT NOT NULL,
  FOREIGN KEY (Buyer_id) REFERENCES Buyer(Buyer_id)
);

CREATE TABLE Product (
  P_id INT NOT NULL PRIMARY KEY,
  Title VARCHAR(20) NOT NULL,
  Description VARCHAR(20) NOT NULL,
  Price DECIMAL(10, 2) NOT NULL,
  Seller_id INT NOT NULL,
  FOREIGN KEY (Seller_id) REFERENCES Seller(Seller_id)
);

CREATE TABLE Payment (
  Payment_id INT NOT NULL PRIMARY KEY,
  Bid_id INT NOT NULL,
  B_id INT NOT NULL,
  Amount INT NOT NULL,
  Payment_time DATETIME NOT NULL,
  FOREIGN KEY (Bid_id) REFERENCES Bids(Bid_id),
  FOREIGN KEY (B_id) REFERENCES Buyer(Buyer_id)
);

CREATE TABLE Bids (
  Bid_id INT NOT NULL PRIMARY KEY,
  B_id INT NOT NULL,
  P_id INT NOT NULL,
  FOREIGN KEY (B_id) REFERENCES Buyer(Buyer_id),
  FOREIGN KEY (P_id) REFERENCES Product(P_id)
);

CREATE TABLE Listings (
  Listing_id INT NOT NULL PRIMARY KEY,
  Seller_id INT NOT NULL,
  Status VARCHAR(20) NOT NULL,
  Start_date DATE NOT NULL,
  End_date DATE NOT NULL,
  FOREIGN KEY (Seller_id) REFERENCES Seller(Seller_id)
);
