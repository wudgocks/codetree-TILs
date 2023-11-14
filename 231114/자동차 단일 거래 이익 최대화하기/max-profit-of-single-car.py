n = int(input())
lst = list(map(int,input().split()))

maxProfit = 0

# 배열을 앞에서부터 순회하며 사는 시점 후보 선택
for i in range(n) :

    # 구매하는 시점의 다음해부터 순회하며 파는 시점의 후보 선택
    for j in range(i + 1, n) :
        profit = lst[j] - lst[i]

        if profit > maxProfit :
            maxProfit = profit

print(maxProfit)