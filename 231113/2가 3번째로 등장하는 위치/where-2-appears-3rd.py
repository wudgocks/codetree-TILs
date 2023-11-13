n = int(input())

idx, cnt = 0, 0

lst = list(map(int,input().split()))

for element in lst :
    idx += 1
    if element == 2 :
        cnt += 1
    if cnt == 3:
        break

print(idx)