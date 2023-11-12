n = int(input())

for i in range(n) :
    a, b = map(int,input().split())
    tmp = 1
    for j in range(a, b + 1) :
        tmp *= j
    print(tmp)