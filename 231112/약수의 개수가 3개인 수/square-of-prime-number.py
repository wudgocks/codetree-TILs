start, end = map(int,input().split())
cnt = 0

for i in range(start, end + 1) :
    divisor_cnt = 0
    for j in range(1, i + 1) :
        if i%j == 0 :
            divisor_cnt += 1
    if divisor_cnt == 3 :
        cnt +=1 

print(cnt)