# 2차원 배열 선언
lst_2d = [
    list(map(int,input().split()))
    for _ in range(2)
]

# 가로 평균 출력
for i in range(len(lst_2d)) :
    rowSum = 0
    for j in range (4) :
        rowSum += lst_2d[i][j]
    
    print(f'{rowSum/4:.1f}', end = " ")
print()

# 세로 평균 출력
for j in range(4) :
    colSum = 0
    for i in range(2) :
        colSum += lst_2d[i][j]
    print(f'{colSum/2:.1f}', end = " ")
print()

# 전체 평균출력
sumVal = 0
for i in range(2) :
    for j in range(4) :
        sumVal += lst_2d[i][j]

print(f'{sumVal/8:.1f}', end = " ")