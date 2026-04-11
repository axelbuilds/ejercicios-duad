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
