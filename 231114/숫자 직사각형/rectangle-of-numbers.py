n,m = map(int,input().split())

# 행 ==> m // 열 ==> n
lst_2d = [
    [0 for _ in range(m)]
    for _ in range(n)
]

number = 1

for i in range(n) :
    for j in range(m) :
        lst_2d[i][j] = number
        print(number, end = " ")
        number += 1
    print()