num = int(input("Write a Number: "))

a = [i for i in range(2, num) if num % i == 0]

def is_prime(x):
    if num > 1:
        if len(a) == 0:
            print("It's a prime number")
        else:
            print("It's not a prime number")
    else:
        print("It's not a prime number")

is_prime(num)