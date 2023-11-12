m = int(input())

# 입력
for _ in range(m) :
    n = int(input())
    count = 0
    while n != 1 :
        # 짝수인 경우
        if n % 2 == 0 :
            n //= 2
        # 홀수인경우
        else :
            n *=3
            n +=1
        count += 1
    print(count)