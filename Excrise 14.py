import numpy as nump

a = int (input("How much lenght do u want ur list: "))
b = list (nump.random.choice(a, a, replace=True))
print(f"This is the random list \n {b}")

def list2(x):
    c = list(set(b))
    return c

d = list2(b)
print(f"This is using set\n{d}")

def list3(x):
    c = []
    for i in x:
        if i not in c:
            c.append(i)
    return c

e = list3(b)
print(f"This is using loops\n {e}")


