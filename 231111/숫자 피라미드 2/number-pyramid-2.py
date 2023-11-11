n = int(input())
tmp = 1

for i in range(n) :
    for j in range(i + 1) :
        print(tmp, end = " ")
        tmp += 1
    print()