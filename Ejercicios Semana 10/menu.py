#Ejercicio Semana 10 - Menu

from actions import (
    add_student,
    view_students,
    view_top_3,
    view_average_score,
    delete_student,
    view_failed_students
)
from data import export_to_csv, import_from_csv

def show_menu(students):
    while True:
        print("\n - Sistema de Informacion de Estudiantes -")
        print("1. Ingresar estudiantes")
        print("2. Ver todos los estudiantes")
        print("3. Ver top 3 estudiantes")
        print("4. Ver promedio general")
        print("5. Exportar datos a CSV")
        print("6. Importar datos desde CSV")
        print("7. Eliminar un estudiante")
        print("8. Ver estudiantes reprobados")
        print("9. Salir")

        option = input("Seleccione una opcion: ")

        if option == "1":
            add_student(students)
        elif option == "2":
            view_students(students)
        elif option == "3":
            view_top_3(students)
        elif option == "4":
            view_average_score(students)
        elif option == "5":
            export_to_csv(students)
        elif option == "6":
            import_from_csv(students)
        elif option == "7":
            delete_student(students)
        elif option == "8":
            view_failed_students(students)
        elif option == "9":
            print("Hasta Luego!")
            break  # Exit the loop and end the program
        else:
            print("Opcion invalida. Selecciona una opcion del 1 al 9.")