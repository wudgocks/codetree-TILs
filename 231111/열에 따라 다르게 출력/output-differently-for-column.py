n = int(input())

tmp = 0

for i in range(n) :
    if i % 2 == 0 :
        for j in range(tmp, n + tmp) :
            tmp  += 1
            print(tmp, end = " ")     
    else :
        for j in range(n) :
            tmp += 2
            print(tmp, end = " ")

    print()