-- SQLite

-- Primary Keys en SQLite

-- Utilice INTEGER PRIMARY KEY AUTOINCREMENT para generar PKs automaticamente.

-- Limitaciones de SQLite
-- No se pueden definir tipos numericos, solo funciona INTEGER.
-- No se puede definir tipos de texto, solo TEXT.
-- No existe Timestamp, solo se puede utilizar TEXT para agregar fechas.

-- Creaci0n de la base de datos:
-- Productos
CREATE TABLE Productos (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT NOT NULL,
    price REAL CHECK(precio >= 0),
    entry_date TEXT,
    brand TEXT
);

-- Users
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    email TEXT UNIQUE,
    creation_date TEXT
);

-- Payment Method
CREATE TABLE metodos_pago (
    method_id INTEGER PRIMARY KEY AUTOINCREMENT,
    method_type TEXT NOT NULL,
    bank_name TEXT
);

-- Invoices
CREATE TABLE facturas (
    invoice_id INTEGER PRIMARY KEY AUTOINCREMENT,
    purchase_date TEXT,
    user_id INTEGER,
    total_amount REAL,
    method_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (method_id) REFERENCES metodos_pago(method_id)
);

-- Invoice Detail
CREATE TABLE detalle_factura (
    invoice_detail_id INTEGER PRIMARY KEY AUTOINCREMENT,
    invoice_id INTEGER,
    product_id INTEGER,
    count INTEGER,
    subtotal_amount REAL,
    FOREIGN KEY (invoice_id) REFERENCES facturas(invoice_id),
    FOREIGN KEY (product_id) REFERENCES productos(product_id)
);

-- Shopping Cart
CREATE TABLE carrito (
    cart_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Shopping Cart Detail
CREATE TABLE detalle_Carrito (
    cart_detail_id INTEGER PRIMARY KEY AUTOINCREMENT,
    cart_id INTEGER,
    product_id INTEGER,
    count INTEGER,
    FOREIGN KEY (cart_id) REFERENCES carrito(cart_id),
    FOREIGN KEY (product_id) REFERENCES productos(product_id)
);

-- Product Reviews
CREATE TABLE reviews (
    review_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER,
    comment TEXT,
    rating INTEGER CHECK(rating BETWEEN 1 AND 5),
    review_date TEXT,
    user_id INTEGER,
    FOREIGN KEY (product_id) REFERENCES productos(product_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);



-- Consultas de datos:

SELECT * FROM productos;

SELECT * FROM productos 
WHERE price > 50000;

SELECT * FROM detalle_factura 
WHERE product_id = 1;

SELECT 
    product_id, 
    SUM(count) AS unidades_vendidas, 
    SUM(subtotal_amount) AS venta_total
FROM detalle_factura
GROUP BY product_id;

SELECT * FROM facturas 
WHERE user_id = 1;

SELECT * FROM facturas 
ORDER BY total_amount DESC;

SELECT * FROM facturas 
WHERE invoice_id = 1;

-- Ejercicios Extra de SQL

-- Category Table
CREATE TABLE categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    description TEXT
);

-- Adding category_id and stock to Productos table
ALTER TABLE productos ADD COLUMN category_id INTEGER REFERENCES categories(id);
ALTER TABLE productos ADD COLUMN stock_available INTEGER DEFAULT 0;

-- Adding categories
INSERT INTO categories (name, description) 
    VALUES
    ('Perifericos', 'Dispositivos de entrada y salida'),
    ('Monitores', 'Pantallas'),
    ('Audio', 'Audifonos y Parlantes');

-- Update existing products with categories
UPDATE productos SET category_id = 1 WHERE product_id IN (1,4);
UPDATE productos SET category_id = 2 WHERE product_id = 2;
UPDATE productos SET category_id = 3 WHERE product_id = 3;

-- Adding new products
INSERT INTO productos (product_name, price, entry_date, brand, stock_available, category_id) 
    VALUES 
    ('Apple MacBook Air', 750000, '18/04/2026', 'Apple', 5, 2),
    ('Apple iPhone 15', 600000, '18/04/2026', 'Apple', 8, 1),
    ('Mouse Pad', 15000, '18/04/2026', 'RedDragon', 50, 1),
    ('Apple AirPods', 120000, '18/04/2026', 'Apple', 15, 3),
    ('Webcam 4K', 45000, '18/04/2026','Logitech', 12, 1),
    ('Silla Gamer', 180000, '18/04/2026', 'Vertager', 3, 1),
    ('Apple Watch', 250000, '18/04/2026', 'Apple', 7, 1),
    ('Cable HDMI', 12000, '18/04/2026', 'Unknown', 100, 2),
    ('Disco SSD 1TB', 55000, '18/04/2026', 'Sandisk', 20, 1),
    ('Parlante Bluetooth', 35000, '18/04/2026', 'Xiaomi', 9, 3);

-- Queries
-- Check all products
SELECT * FROM productos;

-- Filter price > 50,000
SELECT * FROM productos WHERE price > 50000;

-- Filter product name 'apple'
SELECT * FROM productos WHERE product_name LIKE '%apple%';

-- Filter 5 most expensive products
SELECT * FROM productos ORDER BY price DESC LIMIT 5;

-- Product updates

-- Stock to 0 when price <= 0
UPDATE productos SET stock_available = 0 WHERE price <= 0;

-- Increase price by 100 if stock is less than 10
UPDATE productos SET price = price + 100 WHERE stock_available < 10;

-- Decrease stock by 1 for a product
UPDATE productos SET stock_available = stock_available - 1 WHERE product_id = 22;

-- Query all products ordered by id
SELECT * FROM productos ORDER BY product_id ASC LIMIT 10;