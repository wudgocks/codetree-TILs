string = input()

char = string[1]

strLst = list(string)

for i in range(len(strLst)) :
    if strLst[i] == char :
        strLst[i] = strLst[0]

print(''.join(strLst))