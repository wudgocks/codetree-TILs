start, end = map(int, input().split())
cnt = 0

# 비교할 숫자
for i in range(start, end + 1) :
    tmp = 0
    for j in range(1,i) :
        if i % j == 0 :
            tmp += j
    if tmp == i :
        cnt += 1

print(cnt)