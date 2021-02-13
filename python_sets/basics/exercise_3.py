def union(a, b):
    c = []
    c.extend(a)

    for number in b:
        if number not in c:
            c.append(number)
    return c


def union1(a, b):
    # return set(a) | set(b)
    return set(a).union(set(b))


a = [1, 2, 3, 4]
b = [1, 2, 8, 9]
print(union(a, b))
print(union1(a, b))

print(a)
