n = int(input())

arr = list(map(int,input().split()))

counter = 0
for i in range(n) :
    for j in range(i + 1, n) :
        for k in range(j + 1, n) :
            if arr[i] < arr[j] and arr[j] < arr[k] :
                counter += 1

print(counter)