-- Tables creation

CREATE TABLE Authors (
    author_id INTEGER PRIMARY KEY AUTOINCREMENT,
    author_name TEXT NOT NULL
);

CREATE TABLE Customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT NOT NULL,
    customer_email TEXT UNIQUE NOT NULL -- UNIQUE to avoid email dupliacation
);

CREATE TABLE Books (
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_title TEXT NOT NULL,
    author_id INTEGER,
    FOREIGN KEY (author_id) REFERENCES Authors(author_id) ON DELETE SET NULL 
);

CREATE TABLE Rents (
    rent_id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER NOT NULL,
    customer_id INTEGER NOT NULL,
    state TEXT CHECK(state IN('Returned', 'On time', 'Overdue')) NOT NULL,
    FOREIGN KEY (book_id) REFERENCES Books(book_id),
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

-- Data Insertion

INSERT INTO Authors (author_id, author_name) VALUES 
(1, 'Miguel de Cervantes'),
(2, 'Dante Alighieri'),
(3, 'Takehiko Inoue'),
(4, 'Akira Toriyama'),
(5, 'Walt Disney');

INSERT INTO Books (book_id, book_title, author_id) VALUES 
(1, 'Don Quijote', 1),
(2, 'La Divina Comedia', 2),
(3, 'Vagabond 1-3', 3),
(4, 'Dragon Ball 1', 4),
(5, 'The Book of the 5 Rings', NULL);

INSERT INTO Customers (customer_id, customer_name, customer_email) VALUES 
(1, 'John Doe', 'j.doe@email.com'),
(2, 'Jane Doe', 'jane@doe.com'),
(3, 'Luke Skywalker', 'darth.son@email.com');

INSERT INTO Rents (rent_id, book_id, customer_id, state) VALUES 
(1, 1, 2, 'Returned'),
(2, 2, 2, 'Returned'),
(3, 1, 1, 'On time'),
(4, 3, 1, 'On time'),
(5, 2, 2, 'Overdue');


-- JOINs
-- 1. Obtenga todos los libros y sus autores (en caso de tenerlos)
SELECT
    b.book_id,
    b.book_title,
    a.author_id
FROM Books AS b
LEFT JOIN Authors AS a ON b.author_id = a.author_id; 

-- 2. Obtenga todos los libros que no tienen autor
SELECT
    b.book_id,
    b.book_title
FROM Books AS b
LEFT JOIN Authors AS a ON b.author_id = a.author_id
WHERE a.author_id IS NULL;

-- 3. Obtenga todos los autores que no tienen libros
SELECT
    a.author_id,
    a.author_name
FROM Authors AS a
LEFT JOIN Books AS b ON a.author_id = b.author_id
WHERE b.author_id is NULL;

-- 4. Obtenga todos los libros que han sido rentados en algún momento
SELECT
    r.rent_id,
    b.book_title,
    b.book_id
FROM Rents AS R
INNER JOIN Books AS b ON r.book_id = b.book_id;

-- 5. Obtenga todos los libros que nunca han sido rentados
SELECT
    b.book_id,
    b.book_title
FROM Books AS b
LEFT JOIN Rents AS r ON r.book_id = b.book_id
WHERE r.rent_id is NULL;

-- 6. Obtenga todos los clientes que nunca han rentado un libro
SELECT
    c.customer_id,
    c.customer_name
FROM Customers AS c
LEFT JOIN Rents AS r ON c.customer_id = r.customer_id
WHERE r.rent_id is NULL;

-- 7. Obtenga todos los libros que han sido rentados y están en estado “Overdue”
SELECT
    b.book_id,
    b.book_title
FROM Books AS b
LEFT JOIN Rents AS r ON b.book_id = r.book_id
WHERE r.state is 'Overdue';