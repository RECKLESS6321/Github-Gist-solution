a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = int(input("Write a number: "))
new_list = []

new_list = [x for x in a if x < b] 
print(f"Number which are smaller than ur number {b} are {new_list}.")
