n = int(input())

tmp = 1
m = n
for i in range(n, 0, -1) :
    for j in range(m, 0, -tmp) :
        print(j, end = " ")
    print()
    tmp += 1
    m+=n