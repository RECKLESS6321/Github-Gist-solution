# In this fuction we are cutting the string in halve and reseversing the 2nd half while complaing it to the 1st half 
# If the 1st and 2nd is same it return false and true if its not same

def is_palindrome(a):
    for i in range(0, int(len(a)/2)):
        if a[i] != a[len(a)-i-1]:
            return False
    return True

a = input("Write any thing: ")
b = is_palindrome(a)

if b:
    print(f"{a} is a palindrome")
else:
    print(f"{a} is not a palindrome")
