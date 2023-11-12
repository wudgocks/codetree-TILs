# 짝수합 // 3의 배수 번쨰 입력값

lst = list(map(int,input().split()))

sumEv = 0

sum3 = 0
avg3 = 0
cnt3 = 0

for i in range(len(lst)) :
    if (i+1) % 2 == 0 :
        sumEv += lst[i]
    if (i+1) % 3 == 0 :
        sum3 += lst[i]
        cnt3 += 1

print(sumEv, end = " ")
print(f'{sum3/cnt3:.1f}')