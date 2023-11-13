lst = list(map(int,input().split()))

evenSum = 0
oddSum = 0

for i in range(len(lst)) :
    if (i % 2) == 0 :
        evenSum += lst[i]
    else :
        oddSum += lst[i]
        

print(abs(evenSum - oddSum))