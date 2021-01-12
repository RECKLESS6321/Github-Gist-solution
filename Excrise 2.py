num = int(input("Write a number: "))
check = int(input("Write a another number to divided it with: "))

if num % 4 == 0:
    print(f"Your number {num} is divided 4 and was found even")
elif num % 2 == 0:
    print(f"Your number {num} is even")
else:
    print(f"Your number {num} is odd")

if num % check == 0:
    print(f"{num} is divisibel by {check}")
else:
    print(f"{num} is not divisibel by {check}")
