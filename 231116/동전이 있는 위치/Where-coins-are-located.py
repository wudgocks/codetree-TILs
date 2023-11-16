n, m = map(int,input().split())

lst_2d = [
    [0 for _ in range(n)]
    for _ in range(n)
]


for _ in range(m) :
    r, c = tuple(map(int,input().split()))
    lst_2d[r-1][c-1] = 1

for row in lst_2d :
    for elem in row :
        print(elem, end= " ")
    print()