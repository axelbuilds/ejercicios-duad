#Ejercicio de Sintaxis #5

grade_counter = 1
approved_grades_count = 0
failed_grades_count = 0
approved_grades_sum = 0
failed_grades_sum = 0
total_average = 0

total_grades = int(input("Digite la cantidad de notas que desea calcular: "))
if total_grades == 0:
    total_grades = int(input("Digite un numero mayor a 0 empezar el calculo: "))# Defines the amount of grades to calculate

while grade_counter <= total_grades:
    current_grade = int(input(f"Digite la nota número {grade_counter}: "))
    if current_grade < 70:
        failed_grades_count = failed_grades_count + 1
        failed_grades_sum = failed_grades_sum + current_grade
    else:
        approved_grades_count = approved_grades_count + 1
        approved_grades_sum = approved_grades_sum + current_grade
    grade_counter = grade_counter + 1 #Increases the counter

#Averages
if failed_grades_count > 0:
    failed_average = failed_grades_sum / failed_grades_count
else:
    failed_average = 0

if approved_grades_count > 0:
    approved_average = approved_grades_sum / approved_grades_count
else:
    approved_average = 0

total_average = (approved_grades_sum + failed_grades_sum) / total_grades

#Totals/Averages display
print("El estudiante tiene", approved_grades_count, "notas aprobadas.")
print("El promedio de notas aprobadas es:", approved_average)
print("El estudiante tiene", failed_grades_count, "notas desaprobadas.")
print("El promedio de notas desaprobadas es:", failed_average)
print("Este es el promedio total de notas:", total_average)