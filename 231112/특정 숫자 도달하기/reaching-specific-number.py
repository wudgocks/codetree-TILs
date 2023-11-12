# 정수 배열 입력
lst = [*map(int,input().split())]

sumVal = 0
cnt = 0
for element in lst :
    if element >= 250 :
        break
    sumVal += element
    cnt += 1

print(sumVal, end = "")
print(f'{sumVal/cnt : .1f}')