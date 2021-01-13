import random

num = random.randint(1,100)
turn = 0
user = 0
print("Try to guess the number in my Mind")

while user != num and user != "exit" and user != "Exit":
    user = input("Guess a number: ")

    if user == "exit" or user == "Exit":
        turn += 1
        print(f"Thanks for Playing, u took {turn} turn and still was't able to find the number NOOB.")
        break

    user = int(user)
    turn += 1

    if user > num:
        print("Your number is to high")

    elif user < num:
        print("Your number is to low")

    else:
        print("\nCongratz you found the number")
        print(f"It took u {turn} turn to figure out the number")
