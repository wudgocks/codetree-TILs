import sys
minVal = sys.maxsize

n = int(input())

lst = list(map(int,input().split()))
cnt = 0

for element in lst :
    if element < minVal :
        minVal = element
        cnt += 1

print(minVal, cnt)