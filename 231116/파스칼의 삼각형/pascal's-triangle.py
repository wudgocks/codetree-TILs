n = int(input())

lst_2d = [
    [0 for _ in range(n) ]
    for _ in range(n)
]

lst_2d[0][0] = 1

for i in range(1,n) :
    for j in range(i + 1) :
        lst_2d[i][j] = lst_2d[i-1][j-1] + lst_2d[i-1][j]

for row in lst_2d :
    for elem in row :
        if elem != 0 :
            print(elem, end = " ")
    print()