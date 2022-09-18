CREATE DATABASE cm_devices;

USE cm_devices;

CREATE TABLE invoice(
    customerID VARCHAR(50),
    orderDate DATE,
    quantity INT,
    price DECIMAL
);

CREATE TABLE address(
    id INT NOT NULL, 
    street VARCHAR(255), 
    postCode VARCHAR(10) DEFAULT "HA97DE",
    town VARCHAR(30) DEFAULT "Harrow"
);

CREATE TABLE customers(
    username CHAR(9),
    fullName VARCHAR(100), 
    email VARCHAR(255)
);

CREATE TABLE devices(
    deviceID INT,
    deviceName VARCHAR(50),
    price DECIMAL
);

CREATE TABLE account(
    accountNumber INT,
    phoneNumber INT,
    email VARCHAR(255)
);

show tables;

SHOW COLUMNS FROM invoice;

CREATE DATABASE bookshop;

USE bookshop;

CREATE TABLE customers(
    customerID int,
    customerName varchar(50),
    customerAddress varchar(255)
);

SHOW TABLES;

INSERT INTO customers(
    customerID,
    customerName,
    customerAddress
)
VALUES
(1, "Jack", "115 Old street Belfast"),
(2, "James", "24 Carlson Rd London");

SELECT * FROM customers;



TRUNCATE TABLE customers;

INSERT INTO `customers` (
    `customerID`,
    `customerName`,
    `customerAddress`)
VALUES
(1, 'Jack', '115 Old street Belfast'),
(2, 'James', '24 Carlson Rd London'),
(4, 'Maria', '5 Fredrik Rd, Bedford'),
(5, 'Jade', '10 Copland Ave Portsmouth '),
(6, 'Yasmine', '15 Fredrik Rd, Bedford'),
(3, 'Jimmy', '110 Copland Ave Portsmouth');     


DELETE FROM customers 
WHERE customerID = 3;

SELECT * FROM customers;