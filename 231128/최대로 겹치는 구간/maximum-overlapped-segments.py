# 구간의 경우에는 x1부터 x2 - 1까지 표시를 해주면 됩니다.
n = int(input())

checker = [0] * 200

for i in range(n) :
    x1,x2 = tuple(map(int,input().split()))
    for x in range(x1,x2) :
        checker[x] += 1

maxVal = 0

for i in range(len(checker)) :
    maxVal = max(maxVal,checker[i])

print(maxVal)