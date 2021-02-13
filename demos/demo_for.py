ll = [1, 2, 3, 4, 5]
ll2 = [4, 5, 6, 7, 8]

result_list = []
result = 0

for el in ll:
    result += el
    result_list.append(result)

for el in ll2:
    result += el
    result_list.append(result)

print(result)
print(result_list)


result2 = 0
result_list2 = []
for i in range(len(ll)):
    result2 += ll[i] + ll2[i]
    result_list2.append(result2)

print(result2)
print(result_list2)