-- EJERCICIO 1 POSTRESQL


-- SERIAL: Autoincrements the ID automatically
-- VARCHAR: Saves the text limiting the amount of characters in the field
-- UNIQUE: Avoids duplicates
-- CHECK: Checks before saving new values
-- CURRENT_TIMESTAMP: Saves current time and date automatically

-- Table Creation
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,
    user_name VARCHAR(50) NOT NULL,
    user_email VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE Products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(50) NOT NULL,
    product_price INT NOT NULL,
    product_stock INT NOT NULL CHECK (product_stock >= 0)
);

CREATE TABLE Bills (
    bill_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES Users(user_id),
    bill_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    bill_status VARCHAR(20) DEFAULT 'Completada'
);

CREATE TABLE Bill_Details (
    bill_id INT REFERENCES Bills(bill_id),
    product_id INT REFERENCES Products(product_id),
    purchase_quantity INT NOT NULL,
    PRIMARY KEY (bill_id, product_id) -- Avoid duplicates on the same bill
);

-- Data Insertion

-- Users Data
INSERT INTO Users (user_name, user_email) VALUES
('Juan Ramirez', 'juan.ram@email.com'),
('Maria Lopez', 'maria.lop@email.com'),
('Carlos Castro', 'carlos.cast@email.com'),
('Ana Rojas', 'ana.rojas@email.com'),
('Luis Solano', 'luis.solano@email.com');

-- Products Data
INSERT INTO Products (product_name, product_price, product_stock) VALUES
('MAC M2', 650000, 15),
('Mouse Razer', 25000, 40),
('Teclado Logitech', 35000, 20),
('Monitor Gamer 27', 185000, 8),
('Audífonos Senheiser', 95000, 0);

-- Bills Data
INSERT INTO Bills (user_id) VALUES
(1),
(2),
(1),
(3),
(4);

-- Bill Details Data
INSERT INTO Bill_Details (bill_id, product_id, purchase_quantity) VALUES
(1, 1, 1),
(1, 2, 2),
(2, 3, 1),
(3, 4, 1),
(4, 2, 1),
(5, 1, 1);


-- Query Test
SELECT * FROM Users;
SELECT * FROM Products;
SELECT * FROM Bills;
SELECT * FROM Bill_Details;