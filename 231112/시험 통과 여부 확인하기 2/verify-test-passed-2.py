n = int(input())
cnt = 0
for i in range(n) :
    sumVal = 0
    lst = list(map(int,input().split()))
    for element in lst :
        sumVal += element
    if (sumVal/4) >= 60 :
        print("pass")
        cnt +=1 
    else :
        print("fail")
print(cnt)