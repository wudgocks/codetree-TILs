n,m = map(int,input().split())

A = [0] + list(map(int,input().split()))

def temp(arr) :
    global m
    sumNum = 0
    while m :
        sumNum += arr[m]
        if m%2 == 1 :
            m -= 1
        else :
            m //= 2
            
    return sumNum

print(temp(A))