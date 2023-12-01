OFFSET = 500

MAX_R = 1000

# 세개의 사각형 입력
rects = [
    tuple(map(int, input().split()))
    for _ in range(3)
]

# 좌표 평면을 표현한 배열
checked = [
    [0] * (MAX_R + 1)
    for _ in range(MAX_R + 1)
]

tmp = 0
for x1, y1, x2, y2 in rects:
    # OFFSET을 더해줍니다.
    x1, y1 = x1 + OFFSET, y1 + OFFSET
    x2, y2 = x2 + OFFSET, y2 + OFFSET

    for x in range(x1,x2) :
        for y in range(y1,y2) :
            checked[x][y] = 1
    
    tmp += 1

    if tmp == 2 :
        for x in range(x1,x2) :
            for y in range(y1,y2) :
                checked[x][y] = 0
    
areaWidth = 0

for x in range(0, MAX_R + 1) :
    for y in range(0, MAX_R + 1) :
        if checked[x][y] :
            areaWidth +=1 


print(areaWidth)