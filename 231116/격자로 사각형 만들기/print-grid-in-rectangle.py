n = int(input())

lst_2d = [
    [0 for _  in range(n)]
    for _ in range(n)
]

for j in range(n) :
    lst_2d[0][j] = 1

for i in range(n) :
    lst_2d[i][0] = 1

for i in range(1,n) :
    for j in range(1, n) :
        lst_2d[i][j] = lst_2d[i-1][j] + lst_2d[i][j-1] + lst_2d[i-1][j-1]
# 출력
for row in lst_2d :
    for elem in row :
        print(elem, end = " ")
    print()