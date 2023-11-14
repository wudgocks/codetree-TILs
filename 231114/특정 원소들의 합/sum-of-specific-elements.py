# 2차원 배열 선언
lst_2d = [
    list(map(int,input().split()))
    for _ in range(4)
]
sumVal = 0
for i in range(4) :
    for j in range(i + 1) :
        sumVal += lst_2d[i][j]
print(sumVal)