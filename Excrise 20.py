import random

def binary_search(sorted_list, target):
    left_pointer = 0
    right_pointer = len(sorted_list)

    while left_pointer < right_pointer:
        mid_idx = (left_pointer + right_pointer) // 2
        mid_value = sorted_list[mid_idx]

        if mid_value ==  target:
            return mid_idx
        
        if target < mid_value:
            right_pointer = mid_idx
        
        if target > mid_value:
            left_pointer = mid_idx

        if target not in sorted_list :
            return "not"

if __name__ == "__main__":
    ran = list(sorted(set(random.randint(0,100) for i in range(10))))
    print(ran) 
    find = int(input("Which number to find in the random list from 0 to 10: "))
    search = binary_search(ran,find)
    print(f"Your number is {search} in the list")

