def rev_sentence(x):
    b = x.split(' ')
    c = ' '.join(reversed(b))
    return c

a = str(input("write something: "))
d = rev_sentence(a)
print(f"Your sentence reverse is \n {d}")
