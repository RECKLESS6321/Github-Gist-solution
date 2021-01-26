import random

def guess():
    a = 0
    b = 100
    c = random.randint(1,100)
    count = 1
    
    user = int(input("Guess a number from 1 to 100: "))
    comp = int(input(f"\nIs ur number {c}\nIf its high write 0 \nIf its low write 2\nIf it is then write 1: "))
    
    while comp != 1:
        count += 1
    
        if comp == 0:
            b = c
            c = (a + c) // 2

        elif comp == 2:
            a = c
            c = (c + b) // 2
        comp = int(input(f"\nIs ur number {c} \nif its high press 0 \nif its low press 2\nif its ur number press 1: "))

    print(f"\nYour number was {user} and it took {count} turn to find ur number.")

guess()