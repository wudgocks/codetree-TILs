lst = list(map(int,input().split()))
cnt = 0
sumVal = 0
cnt2 = 0

for element in lst :
    if element == 0 :
        break
    cnt += 1

for i in range(cnt) :
    if lst[i] % 2 == 0 :
        sumVal += lst[i]
        cnt2 += 1

print(f'{cnt2} {sumVal}')