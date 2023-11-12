n = int(input())
jsum_lst = []
for _ in range(n) :
    a,b = map(int,input().split())
    jsum = 0
    for j in range(a, b + 1) :
        if j%2 == 0 :
            jsum += j
    jsum_lst.append(jsum)
    jsum = 0

for i in range(n) :
    print(jsum_lst[i])