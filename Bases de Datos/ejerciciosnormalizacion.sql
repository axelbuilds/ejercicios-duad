-- EJERCICIO 1: ORDERS

-- Problemas identificados en la tabla original
-- Datos del cliente repetidos en varias filas.
-- Dirección duplicada en diferentes órdenes.
-- Productos repetidos en varias órdenes.
-- Una orden puede contener varios productos.
-- Información mezclada en una sola tabla.

-- 1FN
-- Se organizaron los datos para que cada campo contenga un solo valor y cada fila represente un producto dentro de una orden.
-- 2FN
-- Se separó la información que dependía únicamente de la Orden o del Producto, creando tablas independientes como Customers, Items y Order Details.
-- 3FN
-- Se eliminaron dependencias innecesarias guardando clientes, productos y direcciones en tablas separadas.

-- Tabla de Clientes
CREATE TABLE Customers (
    CustomerID TEXT PRIMARY KEY, 
    Customer_Name TEXT NOT NULL,
    Customer_Phone TEXT
);

-- Tabla de Direcciones
CREATE TABLE Customer_Address (
    AddressID TEXT PRIMARY KEY,
    CustomerID TEXT,
    Customer_Address TEXT NOT NULL,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

-- Tabla de Productos
CREATE TABLE Items (
    ItemID INTEGER PRIMARY KEY AUTOINCREMENT,
    Item_Name TEXT NOT NULL,
    Price REAL NOT NULL
);

-- Tabla de Ordenes
CREATE TABLE Orders (
    OrderID INTEGER,
    CustomerID TEXT,
    AddressID TEXT,
    Delivery_Time TEXT, -- Almacenado como texto ISO8601 o formato libre
    PRIMARY KEY (OrderID, AddressID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (AddressID) REFERENCES Customer_Address(AddressID)
);

-- Detalle de la Orden
CREATE TABLE OrderDetails (
    OrderDetailID INTEGER PRIMARY KEY AUTOINCREMENT,
    OrderID INTEGER,
    ItemID INTEGER,
    Quantity INTEGER NOT NULL,
    Special_Requests TEXT,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ItemID) REFERENCES Items(ItemID)
);

-- INSERCICION DE DATOS

INSERT INTO Customers VALUES ('C01', 'Alice', '123-456-7890'), ('C02', 'Bob', '987-654-3210'), ('C03', 'Claire', '555-123-4567');

INSERT INTO Customer_Address VALUES 
('A01', 'C01', '123 Main St'), ('A02', 'C02', '456 Elm St'), 
('A03', 'C02', '4th Avenue'), ('A04', 'C03', '789 Oak St'), ('A05', 'C03', '464 Georgia St');

INSERT INTO Items (ItemID, Item_Name, Price) VALUES (101, 'Cheeseburger', 8.0), (102, 'Fries', 3.0), (103, 'Pizza', 12.0), (105, 'Salad', 6.0), (106, 'Water', 1.0);

INSERT INTO Orders VALUES (1, 'C01', 'A01', '18:00:00'), (2, 'C02', 'A02', '19:30:00'), (2, 'C02', 'A03', '19:30:00'), (3, 'C03', 'A04', '12:00:00'), (4, 'C03', 'A05', '17:00:00');

INSERT INTO OrderDetails (OrderID, Item_ID, Quantity, Special_Requests) VALUES (1, 101, 2, 'No onions'), (1, 102, 1, 'Extra ketchup'), (2, 103, 1, 'Extra cheese'), (2, 102, 2, 'None'), (3, 105, 1, 'No croutons'), (4, 106, 1, 'None');


-- EJERCICIO 2: CARS

-- Problemas identificados en la Tabla Original
-- Vehículos repetidos cuando cambian de dueño.
-- Datos del propietario repetidos.
-- Información del seguro repetida.
-- Datos de vehículo, dueño y póliza mezclados en una sola tabla.

-- 1FN
-- Se verificó que todos los campos contienen valores simples y una sola información por celda.
-- 2FN
--  Se separó la información del vehículo y del propietario en tablas independientes para reducir redundancias.
--  3FN
-- Se crearon tablas adicionales para seguros y polizas.
-- Permite actualizar teléfonos, vehículos o seguros sin modificar múltiples registros.


-- LIMPIEZA DE TABLAS ANTERIORES
DROP TABLE IF EXISTS Ownership;
DROP TABLE IF EXISTS Insurance_Plans;
DROP TABLE IF EXISTS Insurance_Policies;
DROP TABLE IF EXISTS Insurance_Companies;
DROP TABLE IF EXISTS Owners;
DROP TABLE IF EXISTS Vehicles;
DROP TABLE IF EXISTS Vehicle_Models;

-- Tabla de Modelos
CREATE TABLE Vehicle_Models (
    ModelID INTEGER PRIMARY KEY AUTOINCREMENT,
    Make TEXT NOT NULL,
    Model TEXT NOT NULL,
    Year INTEGER NOT NULL,
    UNIQUE(Make, Model, Year)
);

-- Tabla de Vehiculos
CREATE TABLE Vehicles (
    VIN TEXT PRIMARY KEY,
    ModelID INTEGER,
    Color TEXT,
    FOREIGN KEY (ModelID) REFERENCES Vehicle_Models(ModelID)
);

-- Tabla de Owners
CREATE TABLE Owners (
    OwnerID INTEGER PRIMARY KEY AUTOINCREMENT,
    Owner_Name TEXT NOT NULL,
    Owner_Phone TEXT
);

-- Tabla de Seguros
CREATE TABLE Insurance_Companies (
    InsuranceID TEXT PRIMARY KEY,
    Company_Name TEXT NOT NULL
);

-- Tabla de Tipos de Polizas
CREATE TABLE Insurance_Policies (
    PolicyID TEXT PRIMARY KEY,
    Policy_Name TEXT NOT NULL
);

-- Tabla de relacion Compañia y Poliza (Insurance_Plans)
CREATE TABLE Insurance_Plans (
    PlanID INTEGER PRIMARY KEY AUTOINCREMENT,
    InsuranceID TEXT,
    PolicyID TEXT,
    FOREIGN KEY (InsuranceID) REFERENCES Insurance_Companies(InsuranceID),
    FOREIGN KEY (PolicyID) REFERENCES Insurance_Policies(PolicyID),
    UNIQUE(InsuranceID, PolicyID)
);

-- Tabla de Propiedad
CREATE TABLE Ownership (
    OwnershipID INTEGER PRIMARY KEY AUTOINCREMENT,
    VIN TEXT,
    OwnerID INTEGER,
    PlanID INTEGER,
    FOREIGN KEY (VIN) REFERENCES Vehicles(VIN),
    FOREIGN KEY (OwnerID) REFERENCES Owners(OwnerID),
    FOREIGN KEY (PlanID) REFERENCES Insurance_Plans(PlanID)
);

-- INSERCION DE DATOS

INSERT INTO Vehicle_Models (Make, Model, Year) VALUES 
('Honda', 'Accord', 2003), 
('Honda', 'CR-V', 2014), 
('Chevrolet', 'Volt', 2015);

INSERT INTO Vehicles (VIN, ModelID, Color) VALUES 
('1HGCM82633A', 1, 'Silver'), 
('5J6RM4H79EL', 2, 'Blue'), 
('1G1RA6EH1FU', 3, 'Red');

INSERT INTO Owners (OwnerID, Owner_Name, Owner_Phone) VALUES 
(101, 'Alice', '123-456-7890'), 
(102, 'Bob', '987-654-3210'), 
(103, 'Claire', '555-123-4567'), 
(104, 'Dave', '111-222-3333');

INSERT INTO Insurance_Companies VALUES 
('I01', 'ABC Insurance'), ('I02', 'XYZ Insurance'), ('I03', 'DEF Insurance'), ('I04', 'GHI Insurance');

INSERT INTO Insurance_Policies VALUES 
('P01', 'Fire & Theft'), ('P02', 'Full Cover'), ('P03', 'Collision'), ('P04', 'Basic Legal');

INSERT INTO Insurance_Plans (InsuranceID, PolicyID) VALUES 
('I01', 'P01'), ('I02', 'P02'), ('I03', 'P03'), ('I04', 'P04');

INSERT INTO Ownership (VIN, OwnerID, PlanID) VALUES 
('1HGCM82633A', 101, 1), 
('1HGCM82633A', 102, 2), 
('5J6RM4H79EL', 103, 3), 
('1G1RA6EH1FU', 104, 4);