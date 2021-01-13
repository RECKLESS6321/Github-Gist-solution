import random

while True:
    print("Enter player \n 1. Rock \n 2. paper \n 3. scissor")
    
    game_dict = {1: 3, 2: 2, 3: 1}
    player = int(input("Enter 1, 2, 3: "))

    while player > 3 or player < 1:
        player = int(input("Please enter a valid number: "))

    comp = random.randint(1, 3)

    if comp == 1: 
        comp_choice_name = 'Rock'
    elif comp == 2: 
        comp_choice_name = 'paper'
    else: 
        comp_choice_name = 'scissor'
          
    print(f"Computer choice is: {comp_choice_name}" ) 

    a = game_dict.get(player)
    b = game_dict.get(comp)
    dif = a - b
    
    if dif in [-1, 2]:
        print('Player Wins.')
    elif dif in [-2, 1]:
        print('Comp Wins.')
    else:
        print('Draw, Please continue.')

    ans = input("Do you wanna play again? (Y/N): ")
    if ans == "N" or ans == "n":
        break    

print("Thanks for playing")
