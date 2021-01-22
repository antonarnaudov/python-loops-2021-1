name = input('Enter your name: ')

grades = []

grade = float(input('Enter grade: '))
while True:
    if 2 <= grade <= 6:
        grades.append(grade)
    else:
        break

    grade = float(input('Enter grade: '))

average_grade = sum(grades) // len(grades)
print(f'{name} graduated. Average grade: {average_grade:.2f}')
