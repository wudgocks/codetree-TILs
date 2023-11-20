string = input()
leng = len(string)

ary = list(string)

while leng > 1 :
    idx = int(input())

    if idx >= leng :
        idx = leng -1
    
    ary.pop(idx)
    leng -= 1
    
    string = ''.join(ary)

    print(string)