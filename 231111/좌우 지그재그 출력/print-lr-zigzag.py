n = int(input())

tmp = 0

for i in range(n) :
    if i % 2 == 0 :
        for j in range(tmp, n + tmp) :
            tmp  += 1
            print(tmp, end = " ")     
    else :
        for j in range(tmp + n, tmp, -1) :
            print(j, end = " ")
        tmp += n
    print()
             
# 짝수번쨰 줄 - tmp + n 부터 1씩 줄여나감