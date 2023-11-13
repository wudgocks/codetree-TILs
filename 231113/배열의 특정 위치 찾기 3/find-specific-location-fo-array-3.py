lst = list(map(int,input().split()))
new_arr = []

for i in range(len(lst)) :
    if lst[i] == 0 :
        break
    new_arr.append(lst[i])

sumVal = 0

for i in range(len(new_arr)-1, len(new_arr)-4, -1) :
    sumVal += new_arr[i]

print(sumVal)