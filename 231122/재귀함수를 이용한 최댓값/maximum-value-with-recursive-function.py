n = int(input())

lst = list(map(int,input().split()))

def maxValue(a) :
    if a == 0 :
        return arr[0]
    
    return max(maxValue(a-1), arr[a])

print(maxValue(n-1))