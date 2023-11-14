n,m = map(int,input().split())

# 배열 두개 입력
arr1 = [
    list(map(int,input().split()))
    for _ in range(n) 
]

arr2 = [
    list(map(int,input().split()))
    for _ in range(n) 
]

# 결과를 출력할 배열 선언
arr_result = [
    [1 for _ in range(m)]
    for _ in range(n)
]


for i in range(n) :
    for j in range(m) :
        if arr1[i][j] == arr2[i][j] :
            arr_result[i][j] = 0

for i in range(n) :
    for j in range(m) :
        print(arr_result[i][j], end = " ")
    print()