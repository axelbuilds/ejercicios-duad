-- 1. NORMALIZACION DE EMPLEADOS Y PROYECTOS
-- ============================================================================
/*
1FN:
- Se definen los Primary Keys para identificar cada registro de forma unica.
- PK: Employee ID, Project ID

2FN:
- Se eliminan las dependencias parciales que dependian de Employee ID y Project ID.
Empleados_Temp (Employee ID [PK], Employee Name, Department, Department Phone)
Proyectos (Project ID [PK], Project Name, Project Budget)
Empleados_Proyectos (Employee ID [PK/FK], Project ID [PK/FK])

3FN:
- Se eliminan las dependencias transitivas que dependian de Department y no directamente del empleado. 
- Se extrae el departamento a su propia tabla.
*/

-- Creacion de Tablas
CREATE TABLE Departamentos (
    department TEXT PRIMARY KEY,
    department_phone TEXT NOT NULL
);

CREATE TABLE Empleados (
    employee_id INTEGER PRIMARY KEY,
    employee_name TEXT NOT NULL,
    department TEXT,
    FOREIGN KEY (department) REFERENCES Departamentos(department)
);

CREATE TABLE Proyectos (
    project_id TEXT PRIMARY KEY,
    project_name TEXT NOT NULL,
    project_budget REAL NOT NULL
);

CREATE TABLE Empleados_Proyectos (
    employee_id INTEGER,
    project_id TEXT,
    PRIMARY KEY (employee_id, project_id),
    FOREIGN KEY (employee_id) REFERENCES Empleados(employee_id),
    FOREIGN KEY (project_id) REFERENCES Proyectos(project_id)
);

-- Insercion de Datos
INSERT INTO Departamentos (department, department_phone) VALUES 
('IT', '2222-2222'),
('Marketing', '1111-1111');

INSERT INTO Empleados (employee_id, employee_name, department) VALUES 
(201, 'Ana Rivera', 'IT'),
(202, 'Luis Mendez', 'Marketing');

INSERT INTO Proyectos (project_id, project_name, project_budget) VALUES 
('P001', 'Web App', 50000),
('P002', 'API REST', 25000),
('P003', 'Campaña TV', 30000);

INSERT INTO Empleados_Proyectos (employee_id, project_id) VALUES 
(201, 'P001'),
(201, 'P002'),
(202, 'P003');



-- 2. NORMALIZACION DE REGISTRO DE CLASES
/*
1FN:
- Se definen los Primary Keys para identificar cada registro de forma unica.
- PK: Student ID, Course Code

2FN:
- Se eliminan dependencias parciales que dependian de Student ID y Course Code.
Estudiantes (Student ID [PK], Student Name)
Cursos_Temp (Course Code [PK], Course Name, Instructor Name, Instructor Email)
Matricula (Student ID [PK/FK], Course Code [PK/FK])

3FN:
- Se eliminan dependencias transitivas que dependian de Instructor Email, el cual a la vez dependia del codigo del curso.
*/

-- Creacion de Tablas
CREATE TABLE Estudiantes (
    student_id INTEGER PRIMARY KEY,
    student_name TEXT NOT NULL
);

CREATE TABLE Instructores (
    instructor_email TEXT PRIMARY KEY,
    instructor_name TEXT NOT NULL
);

CREATE TABLE Cursos (
    course_code TEXT PRIMARY KEY,
    course_name TEXT NOT NULL,
    instructor_email TEXT,
    FOREIGN KEY (instructor_email) REFERENCES Instructores(instructor_email)
);

CREATE TABLE Matricula (
    student_id INTEGER,
    course_code TEXT,
    PRIMARY KEY (student_id, course_code),
    FOREIGN KEY (student_id) REFERENCES Estudiantes(student_id),
    FOREIGN KEY (course_code) REFERENCES Cursos(course_code)
);

-- Insercion de Datos
INSERT INTO Estudiantes (student_id, student_name) VALUES 
(301, 'Marco Gómez'),
(302, 'Carla Ruiz');

INSERT INTO Instructores (instructor_email, instructor_name) VALUES 
('juan@uni.edu', 'Juan Pérez'),
('laura@uni.edu', 'Laura Rojas');

INSERT INTO Cursos (course_code, course_name, instructor_email) VALUES 
('CS101', 'Python I', 'juan@uni.edu'),
('CS102', 'Python II', 'laura@uni.edu');

INSERT INTO Matricula (student_id, course_code) VALUES 
(301, 'CS101'),
(301, 'CS102'),
(302, 'CS101');


-- 3. NORMALIZACION DE HOSPITAL Y CITAS MEDICAS
/*

1FN y 2FN:
- Al tener una clave primaria simple Appointment ID, la tabla cumple con la 1FN y la 2FN por la ausencia de dependencias parciales.

3FN:
- Se identifican y eliminan dependencias transitivas importantes que dependian de Patient Phone y Doctor Name.
*/

-- Creacion de Tablas (3FN)
CREATE TABLE Pacientes (
    patient_phone TEXT PRIMARY KEY,
    patient_name TEXT NOT NULL
);

CREATE TABLE Medicos (
    doctor_name TEXT PRIMARY KEY,
    specialty TEXT NOT NULL
);

CREATE TABLE Citas (
    appointment_id TEXT PRIMARY KEY,
    patient_phone TEXT,
    doctor_name TEXT,
    date_time TEXT,
    FOREIGN KEY (patient_phone) REFERENCES Pacientes(patient_phone),
    FOREIGN KEY (doctor_name) REFERENCES Medicos(doctor_name)
);

-- Insercion de Datos
INSERT INTO Pacientes (patient_phone, patient_name) VALUES 
('8888-1111', 'Diana Vargas'),
('8999-2222', 'Edwin Mora');

INSERT INTO Medicos (doctor_name, specialty) VALUES 
('Dr. Soto', 'Pediatría'),
('Dr. Mora', 'Cardiología');

INSERT INTO Citas (appointment_id, patient_phone, doctor_name, date_time) VALUES 
('A01', '8888-1111', 'Dr. Soto', '2024-08-01 10:00 AM'),
('A02', '8888-1111', 'Dr. Soto', '2024-08-10 10:00 AM'),
('A03', '8999-2222', 'Dr. Mora', '2024-08-05 01:00 PM');
