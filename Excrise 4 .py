num = int(input("Write a number: "))
divisor_list = []

list2 = list(range(1, num + 1))
for a in list2:
    if num % a == 0:
        divisor_list.append(a)

print(divisor_list)
