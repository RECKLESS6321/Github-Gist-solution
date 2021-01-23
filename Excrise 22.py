view_dict = {}

with open("jason.txt") as j:
    line = j.readline()

    while line:
        line = line[3:-26]
        
        if line in view_dict:
            view_dict[line] += 1
        
        else:
            view_dict[line] = 1
        
        line = j.readline()

print(view_dict)
