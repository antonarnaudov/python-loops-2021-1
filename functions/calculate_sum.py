# def calculate_sum(num1, num2):
#     return f'{num1} + {num2} = {num1 + num2}'
#
#
# print(calculate_sum(2, 5))


def summary(first_element, second_element, *args):
    result = 0

    for number in args:
        result = result + number

    print(first_element, result)
    print(second_element)


summary('gosho', 400, 3, 15, 25)
summary('penka', 400, 3, 15, 25, 123, 400, 3, 15, 25)

ll = [200, 100, 400, 300, 560, 690]

for i in range(len(ll)):
    element = ll[i]
    print(element)
