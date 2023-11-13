n = int(input())

lst = list(map(int,input().split()))

# 처음 2개의 원소 중 더 큰 값을 max1, 더 작은 값을 max2에
if lst[0] > lst[1] :
    max1, max2 = lst[0], lst[1]
else :
    max2, max1 = lst[0], lst[1]

# lst[2]부터 비교하면서 max1, max2를 갱신
for i in range(2, n) :
    if lst[i] >= max1 :
        max2,max1 = max1, lst[i]
    elif lst[i] > max2 :
        max2 = lst[i]

print(max1,max2)