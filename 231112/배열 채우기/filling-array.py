lst = list(map(int,input().split()))
cnt = 0

for elem in lst :
    if elem == 0 :
        break
    cnt += 1

for i in range(cnt-1, -1, -1) :
    print(lst[i], end = " ")