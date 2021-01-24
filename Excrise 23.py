def file_to_read(file_name):
    a = []
    with open(file_name) as b:
        line = b.readline()

        while line:
            a.append(int(line))
            line = b.readline()
    return a

prime = file_to_read("prime.txt")
happy = file_to_read("happy.txt")

over_lapping = [i for i in prime if i in happy]
print(over_lapping)