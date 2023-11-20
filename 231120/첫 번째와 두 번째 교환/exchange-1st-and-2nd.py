string = input()

fst = string[0]
scd = string[1]

lst = []

for i in range(len(string)) :
    if string[i] == fst :
        lst.append(scd)
    elif string[i] == scd :
        lst.append(fst)
    else :
        lst.append(string[i])

print(''.join(lst))