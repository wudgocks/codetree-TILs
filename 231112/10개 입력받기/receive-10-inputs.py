lst = list(map(int,input().split()))
cnt = 0
sumVal = 0

for element in lst :
    if element == 0 :
        break
    cnt += 1

for i in range(cnt) :
    sumVal += lst[i]

print(sumVal, end = " ")
print(f'{sumVal/cnt:.1f}')