n,k = map(int,input().split())

# 블록 칸 배열
lst = [0 for _ in range(n)]

for i in range(k) :
    a,b = tuple(map(int,input().split()))
    for j in range(a-1,b) :
        lst[j] += 1

maxBlock = lst[0]

for element in lst :
    if element >= maxBlock :
        maxBlock = element

print(maxBlock)