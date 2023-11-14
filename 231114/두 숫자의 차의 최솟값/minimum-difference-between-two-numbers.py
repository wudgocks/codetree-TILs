n = int(input())

lst = list(map(int,input().split()))
minNum = 100

for i in range(n) :
    for j in range (i + 1, n) :
        minval = lst[j] - lst[i]
        if minval < minNum :
            minNum = minval

print(minNum)