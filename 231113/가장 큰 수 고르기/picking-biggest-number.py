import sys
# 가장 작은 초깃값을 지정
max_val = -sys.maxsize

lst = list(map(int,input().split()))

for elem in lst :
    if elem > max_val :
        max_val = elem

print(max_val)