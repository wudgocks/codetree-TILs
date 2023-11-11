n,m = map(int,input().split())
num = m
for i in range(1, 9+1) :
    for j in range(m // n) :
        print(f"{num} * {i} = {num*i} " , end = "")
        num -= 2
        if j != m//n -1:
            print("/", end=" ")
    num = m
    print()