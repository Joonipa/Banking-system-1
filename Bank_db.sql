CREATE DATABASE banking_system;

USE banking_system;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    account_number BIGINT UNIQUE NOT NULL,
    dob DATE NOT NULL,
    city VARCHAR(50),
    password VARCHAR(255) NOT NULL,
    balance DECIMAL(10, 2) DEFAULT 2000,
    contact_number VARCHAR(15),
    email VARCHAR(50) UNIQUE,
    address TEXT
);

CREATE TABLE transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    account_number BIGINT NOT NULL,
    transaction_type ENUM('Credit', 'Debit') NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
