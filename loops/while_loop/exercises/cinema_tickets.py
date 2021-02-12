sum = 0
count = 4
while count > 0:
    age = int(input('Enter age: '))
    # if age > 3 and age < 12:
    if 3 < age < 12:
        sum += 10
    elif age > 12:
        sum += 15
    count -= 1

print('Sum = ', sum)
