n,t = map(int,input().split())
arr = list(map(int,input().split()))

ans, counter = 0,0

for i in range(len(arr)) :
    if arr[i] > t :
        counter +=1 
    else :
        counter = 1
    ans = max(ans,counter)

print(counter)