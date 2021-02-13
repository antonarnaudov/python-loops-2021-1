def sum_nums(a, b):
    return a + b


def set_elements_sum(a, b):
    sum_set = []
    for i in range(len(a)):
        # result = a[i] + b[i]

        sum_set.append(a[i] + b[i])

    return sum_set


ll = [1, 2, 3, 4, 5]
ll2 = [4, 5, 6, 7, 8]
print(set_elements_sum(ll, ll2))
