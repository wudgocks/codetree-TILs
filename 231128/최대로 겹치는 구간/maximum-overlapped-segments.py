OFFSET = 100
MAX_R = 200

n = int(input())
checker = [0] * (MAX_R + 1)

for i in range(n) :
    x1,x2 = tuple(map(int,input().split()))
    x1,x2 = x1 + OFFSET, x2 + OFFSET
    for x in range(x1,x2) :
        checker[x] += 1

maxVal = 0

for i in range(len(checker)) :
    maxVal = max(maxVal,checker[i])

print(maxVal)