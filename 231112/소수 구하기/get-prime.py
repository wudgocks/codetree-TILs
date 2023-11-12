n = int(input())
# 나누어 떨어지면 소수가 아님
# i는 확인할 숫자 
# j는 소수를 판별하기 위해 나눌 숫자

for i in range(2, n + 1) :
    isPrime = True
    for j in range(2, i) :
        if i % j == 0 :
            isPrime = False
    if isPrime :
        print(i, end = " ")