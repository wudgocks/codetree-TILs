arr1 = [
    list(map(int,input().split()))
    for _ in range(3) 
]

space = input()

arr2 = [
    list(map(int,input().split()))
    for _ in range(3)
]

arr_result = [
    [0 for _ in range(3)]
    for _ in range(3)
]

for i in range(3) :
    for j in range (3) :
        arr_result[i][j] += arr1[i][j] * arr2[i][j]

for i in range(3) :
    for j in range(3) :
        print(arr_result[i][j], end = " ")
    print()