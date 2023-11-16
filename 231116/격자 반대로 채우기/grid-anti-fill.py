n = int(input())

arr_2d = [
    [ 0 for _ in range(n)]
    for _ in range(n)
]

number = 1

for i in range(n-1,-1,-1) :
    if i%2 == 1 :
        for j in range(n-1,-1,-1) :
            arr_2d[j][i] = number
            number += 1
    else :
        for j in range(n) :
            arr_2d[j][i] = number 
            number += 1


for i in range(n) :
    for j in range(n) :
        print(arr_2d[i][j], end = " ")
    print()