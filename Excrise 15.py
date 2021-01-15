def rev_sentence(x):
    b = x.split(' ')
    return ' '.join(reversed(b))


a = str(input("write something: "))
d = rev_sentence(a)
print(f"Your sentence reverse is \n {d}")