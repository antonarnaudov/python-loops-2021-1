def difference(a, b):
    c = []
    for el in a:
        if el not in b:
            c.append(el)
    return c


ll = [1, 2, 3, 4, 5]
ll2 = [4, 5, 6, 7, 8]

# print(difference(ll, ll2))

# = CTRL + /
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set_difference = set1.difference(set2)
# print(set_difference)

# print(difference(ll, ll2) == list(set_difference))
