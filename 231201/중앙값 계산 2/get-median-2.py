n = int(input())
arr = list(map(int,input().split()))

sortedArr = []

for i in range(len(arr)) :
    if i % 2 == 0 :
        sortedArr.append(arr[i])
        sortedArr.sort()
        print(sortedArr[len(sortedArr)//2], end = " ")
    else :
        sortedArr.append(arr[i])
        sortedArr.sort()
        

# {arr[len(arr)//2]}.")