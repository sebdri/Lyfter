total_grades = int(input("Ingrese la cantidad total de notas:"))

grade_counter = 1

approved_count = 0
failed_count = 0

approved_sum = 0
failed_sum = 0
total_sum = 0

while grade_counter <= total_grades:
    print("Ingrese la nota número:", grade_counter)
    current_grade = float(input())

    total_sum += current_grade

    if current_grade < 70:
        failed_count += 1
        failed_sum += current_grade
    else:
        approved_count += 1
        approved_sum += current_grade

    grade_counter += 1

average_total = total_sum / total_grades

if approved_count > 0:
    average_approved = approved_sum / approved_count
else:
    average_approved = 0

if failed_count > 0:
    average_failed = failed_sum / failed_count
else:
    average_failed = 0

print("El estudiante tiene esta cantidad de notas aprobadas:", approved_count)
print("Este es el promedio de notas aprobadas:", average_approved)
print("El estudiante tiene esta cantidad de notas reprobadas:", failed_count)
print("Este es el promedio de notas reprobadas:", average_failed)
print("Este es el promedio total:", average_total)
