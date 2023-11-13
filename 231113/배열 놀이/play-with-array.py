# 입력 => n개의 원소와 q개의 질의

# 첫번째 줄에는 원소의 개수를 나타내는 n / 질의의 수를 나타내는 q
# 두번째 줄부터 n개의 원소가 공백을 사이에 두고 
# 세번째 줄부터 q개의 줄에 걸쳐 질의

# 첫번쨰줄
n, q = map(int,input().split())
# 두번째줄
lst = list(map(int,input().split()))
# 세번째줄
for i in range(q) :
    inLst = list(map(int,input().split())) # 입력 
    
    # 1번질의 
    if inLst[0] == 1 : 
        print(lst[inLst[1]-1])
     # 2번질의 
    if inLst[0] == 2 :
        for j in range(len(lst)) :
            if lst[j] == inLst[1] : 
                print(j + 1)
                break
            if inLst[1] not in lst :
                print(0)
                break
    if inLst[0] == 3:
        a,b = inLst[1]-1, inLst[2]-1
        for j in range(a,b + 1) :
            print(lst[j], end = " ")
        print()