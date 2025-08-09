#Ejercicio Semana 10 - Actions

import re

def valid_name(name): #Checks that the name is not empty and contains only letters and spaces.
    return name.replace(" ", "").isalpha() #.isalpha ensure all characters are letters


def valid_section(section): #Checks that students section has the valid format: two digits + one uppercase letter
    return bool(re.match(r"^\d{2}[A-Z]$", section)) #re.match(pattern, string) '^' states the start and '$' the end


def student_exists(students, name, section): #Checks if a student with the same name and section already exists.
    return any(s["name"].lower() == name.lower() and s["section"].upper() == section.upper() for s in students)


def input_score(subject): #Requests the user to input a score between 0 and 100, and validates the input.
    while True:
        try:
            score = float(input(f"Ingrese la nota de {subject} (0-100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Numero invalido. La nota debe ser entre 0 y 100.")
        except ValueError:
            print("Entrada invalida. Debe ingresar un numero.")


def add_student(students): #Adds a new student to the list after validating all fields.
    name = input("Ingrese el nombre completo del estudiante: ").strip()
    while not valid_name(name):
        print("Nombre invalido. El nombre no puede esta en blanco ni contener numeros.")
        name = input("Ingrese el nombre completo del estudiante: ").strip()

    section = input("Ingrese la seccion (ejemplo: 11B): ").upper().strip()
    while not valid_section(section):
        print("Seccion invalida. Ejemplo correcto: 10A, 11B.")
        section = input("Ingrese la seccion: ").upper().strip()

    if student_exists(students, name, section):
        print("\n - Ya existe un estudiante con ese nombre y seccion. -")
        return

    # Prompt for scores
    spanish = input_score("Español")
    english = input_score("Ingles")
    history = input_score("Estudios Sociales")
    science = input_score("Ciencias")

    students.append({
        "name": name,
        "section": section,
        "spanish": spanish,
        "english": english,
        "history": history,
        "science": science
    })
    print(f"Estudiante '{name}' agregado correctamente.")


def view_students(students):# Displays all students with their information.
    if not students:
        print("\n - No hay estudiantes registrados. -")
        return
    for s in students:
        print(f"{s['name']} | {s['section']} | Español: {s['spanish']} | Inglés: {s['english']} | Estudios Sociales: {s['history']} | Ciencias: {s['science']}")


def calculate_average(student): #Calculates the general average score of a student.
    return (student["english"] + student["history"] + student["science"]) / 4


def view_top_3(students): #Displays the top 3 students based on their average score.
    if len(students) < 3:
        print("\n - No hay suficientes estudiantes para calcular el top 3. -")
        return
    sorted_students = sorted(students, key=lambda s: calculate_average(s), reverse=True)[:3]
    print("\n Top 3 estudiantes:")
    for s in sorted_students:
        print(f"{s['name']} ({s['section']}) - Promedio: {calculate_average(s):.2f}")


def view_average_score(students): #Displays the overall average score of all students.
    if not students:
        print("\n - No hay estudiantes para calcular el promedio. -")
        return
    average = sum(calculate_average(s) for s in students) / len(students)
    print(f"\n Promedio general de estudiantes: {average:.2f}")


def delete_student(students): #Deletes a student by name and section after confirmation.
    name = input("Ingrese el nombre del estudiante a eliminar: ").strip()
    section = input("Ingrese la seccion del estudiante: ").upper().strip()

    for s in students:
        if s["name"].lower() == name.lower() and s["section"] == section:
            confirm = input(f"¿Está seguro que desea eliminar a {name} ({section})? Escriba: (Si/No): ").lower()
            if confirm == "si":
                students.remove(s)
                print("Estudiante eliminado.")
            else:
                print("Eliminacion cancelada.")
            return
    print("\n - Estudiante no encontrado. -")


def view_failed_students(students): #Shows students who failed at least one subject score less than 60
    print("\n Estudiantes reprobados:")
    failed_found = False
    for s in students:
        failed_subjects = {sub: score for sub, score in {
            "Español": s["spanish"],
            "Inglés": s["english"],
            "Estudios Sociales": s["history"],
            "Ciencias": s["science"]
        }.items() if score < 60}

        if failed_subjects:
            failed_found = True
            print(f"\n{s['name']} ({s['section']}) reprobado:")
            for subject, score in failed_subjects.items():
                print(f" - {subject}: {score}")
    if not failed_found:
        print("n\ - No hay estudiantes reprobados. -")
