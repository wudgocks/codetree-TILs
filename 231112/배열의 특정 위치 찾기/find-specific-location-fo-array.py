# 짝수합 // 3의 배수 번쨰 입력값

lst = list(map(int,input().split()))

sumEv = 0

sum3 = 0
avg3 = 0
cnt3 = 0

for element in lst :
    if element % 2 == 0 :
        sumEv += element
    if element % 3 == 0 :
        sum3 += element
        cnt3 += 1

print(sumEv, end = " ")
print(f'{sum3/cnt3:.1f}')