-- 1. NORMALIZACION DE EMPLEADOS Y PROYECTOS
-- ============================================================================
/*
1FN:
- Se definen Primary Keys para indentificar cada registro de forma unica.
- PK: employee_id, project_id

2FN:
- Se eliminan las dependencias parciales. employee_name y los datos de departamento dependian solo de employee_id. project_name y project_budget dependian de project_id.

3FN:
- Se eliminan dependencias transitivas que dependian de Departament y no directamente del empleado.
- Se crea la tabla Departments con un department_id como PK
*/

-- Creacion de Tablas


CREATE TABLE Departments (
    department_id INTEGER PRIMARY KEY AUTOINCREMENT,
    department_name TEXT NOT NULL,
    department_phone TEXT NOT NULL
);

CREATE TABLE Employees (
    employee_id INTEGER PRIMARY KEY,
    employee_name TEXT NOT NULL,
    department_id INTEGER,
    FOREIGN KEY (department_id) REFERENCES Departments(department_id)
);

CREATE TABLE Projects (
    project_id TEXT PRIMARY KEY,
    project_name TEXT NOT NULL,
    project_budget REAL NOT NULL
);

CREATE TABLE Employee_Projects (
    employee_id INTEGER,
    project_id TEXT,
    PRIMARY KEY (employee_id, project_id),
    FOREIGN KEY (employee_id) REFERENCES Employees(employee_id),
    FOREIGN KEY (project_id) REFERENCES Projects(project_id)
);

-- Insercion de Datos
INSERT INTO Departments (department_name, department_phone) VALUES 
('IT', '2222-2222'),       
('Marketing', '1111-1111');

INSERT INTO Employees (employee_id, employee_name, department_id) VALUES 
(201, 'Ana Rivera', 1),
(202, 'Luis Mendez', 2);

INSERT INTO Projects (project_id, project_name, project_budget) VALUES 
('P001', 'Web App', 50000),
('P002', 'API REST', 25000),
('P003', 'Campaña TV', 30000);

INSERT INTO Employee_Projects (employee_id, project_id) VALUES 
(201, 'P001'),
(201, 'P002'),
(202, 'P003');


-- 2. NORMALIZACION DE REGISTRO DE CLASES
/*
1FN:
- Se definen Primary Keys para indentificar cada registro de forma unica.
- PK: student_id, course_code

2FN:
- Se eliminan dependencias parciales.

3FN:
- Se eliminan dependencias transitivas que dependian del instructor_email.
*/

-- Creacion de Tablas

CREATE TABLE Students (
    student_id INTEGER PRIMARY KEY,
    student_name TEXT NOT NULL
);

CREATE TABLE Instructors (
    instructor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    instructor_name TEXT NOT NULL,
    instructor_email TEXT NOT NULL
);

CREATE TABLE Courses (
    course_code TEXT PRIMARY KEY,
    course_name TEXT NOT NULL,
    instructor_id INTEGER,
    FOREIGN KEY (instructor_id) REFERENCES Instructors(instructor_id)
);

CREATE TABLE Enrollments (
    student_id INTEGER,
    course_code TEXT,
    PRIMARY KEY (student_id, course_code),
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_code) REFERENCES Courses(course_code)
);

-- Insercion de Datos 2
INSERT INTO Students (student_id, student_name) VALUES 
(301, 'Marco Gómez'),
(302, 'Carla Ruiz');

INSERT INTO Instructors (instructor_name, instructor_email) VALUES 
('Juan Pérez', 'juan@uni.edu'), 
('Laura Rojas', 'laura@uni.edu');

INSERT INTO Courses (course_code, course_name, instructor_id) VALUES 
('CS101', 'Python I', 1),
('CS102', 'Python II', 2);

INSERT INTO Enrollments (student_id, course_code) VALUES 
(301, 'CS101'),
(301, 'CS102'),
(302, 'CS101');


-- 3. NORMALIZACION DE HOSPITAL Y CITAS MEDICAS
/*
1FN y 2FN:
- Al tener una clave primaria simple appointment_id, la tabla original cumple con la 1FN y la 2FN por la ausencia de dependencias parciales.

3FN:
- Se eliminan dependencias transitivas donde los datos del paciente y del médico dependian de la cita de forma indirecta.
- Se agrega patient_id y doctor_id como PK AUTOINCREMENT
*/

-- Creacion de Tablas

CREATE TABLE Patients (
    patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_name TEXT NOT NULL,
    patient_phone TEXT NOT NULL
);

CREATE TABLE Doctors (
    doctor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    doctor_name TEXT NOT NULL,
    specialty TEXT NOT NULL
);

CREATE TABLE Appointments (
    appointment_id TEXT PRIMARY KEY,
    patient_id INTEGER,
    doctor_id INTEGER,
    date_time TEXT,
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id)
);

-- Insercion de Datos 3
INSERT INTO Patients (patient_name, patient_phone) VALUES 
('Diana Vargas', '8888-1111'),
('Edwin Mora', '8999-2222');

INSERT INTO Doctors (doctor_name, specialty) VALUES 
('Dr. Soto', 'Pediatría'),
('Dr. Mora', 'Cardiología'); 

INSERT INTO Appointments (appointment_id, patient_id, doctor_id, date_time) VALUES 
('A01', 1, 1, '2024-08-01 10:00 AM'),
('A02', 1, 1, '2024-08-10 10:00 AM'),
('A03', 2, 2, '2024-08-05 01:00 PM');