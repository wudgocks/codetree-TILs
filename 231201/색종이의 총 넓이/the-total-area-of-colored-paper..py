OFFSET = 50

MAX_R = 100
n = int(input())

# 좌표 평면을 표현한 배열
area = [
    [0] * (MAX_R + 1)
    for _ in range(MAX_R + 1)
]

for i in range(n) :
    x,y = tuple(map(int,input().split()))
    x,y = x + OFFSET, y +OFFSET
    
    for i in range(x,x + 8) :
        for j in range(y,y + 8) :
            area[i][j] = 1
    
areaWidth = 0

for x in range(0, MAX_R + 1) :
    for y in range(0, MAX_R + 1) :
        if area[x][y] == 1 :
            areaWidth +=1 

print(areaWidth)