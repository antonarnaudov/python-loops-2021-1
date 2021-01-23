name = input('Enter your name: ')

grades = []


current_grade = float(input('Enter your grade: '))

while True:
    if 2 <= current_grade <= 6:
        grades.append(current_grade)
    else:
        break

    current_grade = float(input('Enter your grade: '))

average_grade = sum(grades) / len(grades)
print(f'{name} graduated. Average grade: {average_grade:.2f}')
