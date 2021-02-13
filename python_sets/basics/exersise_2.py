from python_sets.basics.exercise_1 import is_empty


def is_subset(a, b):
    if is_empty(a) and is_empty(b):
        return True

    for item in a:
        if item not in b:
            return False

    return True


# print(is_subset([1, 2, 3], [1, 2, 3, 4]))

def is_subset1(a, b):
    return a <= b


print(is_subset1([], []))

