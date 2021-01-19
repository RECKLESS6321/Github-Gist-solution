import random

def compare_number(number, player):
    cow = 0
    bull = 0
    for x in range(0,len(number)):
        if number[x] == player[x]:
            bull += 1
        elif player[x] in number:
            cow += 1

    print(f"You have {cow} cow and {bull} bull")


if __name__=="__main__":
    number = str(random.randint(0,9999))
    print(number)
    turn = 0
    print("For every number in the wrong place, you get a cow. For every one in the right place, you get a bull.")

    while(True):
        player = input("Guess a 4 digit number or press 'exit' to exit game: ")
        turn += 1
        if player == "exit" or player == "Exit":
            break
        if player == number:
            print(f"Congrats u found  the number, It took u {turn} turn to find it.")
            break
        else:
            compare_number(number, player)
