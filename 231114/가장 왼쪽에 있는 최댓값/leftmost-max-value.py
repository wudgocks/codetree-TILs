n = int(input())
lst = list(map(int,input().split()))

maxVal = -1
idx = 0

while True :
    # 인덱스 찾기
    for i in range(len(lst)) :
        if lst[i] > maxVal :
            maxVal = lst[i]
            idx = i
    
    for i in range(idx,len(lst)) :
        lst[i] = 0
    
    maxVal = -1
    print(idx + 1, end = " ")

    if idx == 0 :
        break