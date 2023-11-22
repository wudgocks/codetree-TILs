def absNum(arr) :
    for i in range(len(arr)) :
        arr[i] = abs(arr[i])
    
    for i in range(n) :
        print(arr[i], end = " ")

n = int(input())
_list = list(map(int, input().split()))

absNum(_list)