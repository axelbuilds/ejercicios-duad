#Ejercicio Semana 10 - Data

import csv
import os

base_directory = os.path.dirname(os.path.abspath(__file__)) #Gets the path of the current file (data.py) to store the csv file
FILE_NAME = "students_data.csv"  # CSV file name


def export_to_csv(students): #Exports the student list to a CSV file.
    if not students:
        print("n\ - No hay estudiantes para exportar. -")
        return
    with open(FILE_NAME, mode="w", newline="", encoding="utf-8") as file:
        # File Headers
        fieldnames = ["Nombre", "Seccion", "Español", "Ingles", "Estudios Sociales", "Ciencias"]
        writer = csv.writer(file)
        writer.writerow(fieldnames) #Write headers in spanish
        for s in students: #Write information using internal keys
            writer.writerow([s["name"], s["section"], s["spanish"], s["english"], s["history"], s["science"]])
    print(f"Datos exportados a {FILE_NAME}")


def import_from_csv(students): #Imports student data from a CSV file if it exists.
    if not os.path.exists(FILE_NAME):
        print("\n - No existe un archivo CSV previo. Exporte datos primero. -")
        return
    with open(FILE_NAME, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        students.clear()  #Clears current student list before importing
        for row in reader:
            students.append({
                "name": row["Nombre"],
                "section": row["Seccion"],
                "spanish": float(row["Español"]),
                "english": float(row["Ingles"]),
                "history": float(row["Estudios Sociales"]),
                "science": float(row["Ciencias"])
            })
    print(f"Datos importados desde {FILE_NAME}")