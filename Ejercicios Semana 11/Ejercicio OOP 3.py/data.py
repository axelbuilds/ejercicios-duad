#Ejercicio Semana 10 - Data

import csv
import os
from actions import Students, student_list #Import Student class

def export_to_csv(students,FILE_NAME): #Exports the student list to a CSV file.
    if not students:
        print("n\ - No hay estudiantes para exportar. -")
        return
    with open(FILE_NAME, mode="w", newline="", encoding="utf-8") as file:
        # File Headers
        fieldnames = ["Nombre", "Seccion", "Español", "Ingles", "Estudios Sociales", "Ciencias"]
        writer = csv.writer(file)
        writer.writerow(fieldnames) #Write headers in spanish
        for s in students: #Write information using internal keys
            writer.writerow([s.object_to_dictionary]) #Use objects to dictionary
    print(f"Datos exportados a {FILE_NAME}")


def import_from_csv(students,FILE_NAME): #Imports student data from a CSV file if it exists.
    if not os.path.exists(FILE_NAME):
        print("\n - No existe un archivo CSV previo. Exporte datos primero. -")
        return
    with open(FILE_NAME, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        students.clear()  #Clears current student list before importing
        for row in reader:
            students.append(student_list)
    print(f"Datos importados desde {FILE_NAME}")