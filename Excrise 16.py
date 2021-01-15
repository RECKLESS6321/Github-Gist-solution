import random
import string

def password_generator():
    a = str(input("Do u want a weak or strong password: "))
    while a != "weak" or a != "Weak" and a != "strong" or a != "Strong":
        if a == a == "weak" or a == "Weak":
            b = ["Weak", "Noob", "Shit", "Baka", "Dota", "Cry"]
            return random.choice(b)
        if a == "strong" or a == "Strong":
            size = int(input("How much length do you want: "))
            chars=string.ascii_letters + string.digits + string.punctuation
            return ''.join(random.choice(chars) for i in range(size))
        else:
            print("Enter a valid answer")
            a = str(input("Do u want a weak or strong password: "))
            

c = password_generator()
print(c)