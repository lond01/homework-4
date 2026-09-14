def student_grade(name, *grades):
    average = sum(grades) / len(grades)
    print(f"Студент: {name}")
    print(f"Середній бал: {average}")


student_grade("Саша", 10, 11, 9, 12, 10)
