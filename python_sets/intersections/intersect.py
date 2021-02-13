def intersect(a, b):
    intersection = []

    for element in a:
        if element in b:
            intersection.append(element)
    #
    # for element in b:
    #     if element not in a:
    #         intersection.append(element)

    return intersection


ll = [1, 2, 3, 4, 5]
ll2 = [4, 5, 6, 7, 8]

ll_intersection = intersect(ll, ll2)
print(ll_intersection)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
inter_set = set1.intersection(set2)
print(list(inter_set))
