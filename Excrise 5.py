import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

common_list = list(set(i for i in a if i in b))
print(common_list)

c = [random.randint(0,11) for i in range(10)]
d = [random.randint(0,11) for i in range(10)]

random_common_list = list(set(i for i in c if i in d))
print(random_common_list)
