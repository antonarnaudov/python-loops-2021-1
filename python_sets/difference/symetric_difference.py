from python_sets.difference.difference import difference


def symmetric_difference(x, y):
    return difference(x, y) + difference(y, x)


ll = [1, 2, 3, 4, 5]
ll2 = [4, 5, 6, 7, 8]

print(symmetric_difference(ll, ll2), 'from function')

a = difference(ll, ll2)
b = difference(ll2, ll)
c = a + b

print(a, b, 'a and b difference')
print(c, 'a + b difference')

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set_symmetric_difference = set1.symmetric_difference(set2)
print(set_symmetric_difference, 'set difference')
