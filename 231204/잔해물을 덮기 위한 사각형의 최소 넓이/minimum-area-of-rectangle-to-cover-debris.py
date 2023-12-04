OFFSET = 1000
MAX_R = 2000

# 두개의 사각형 입력
rects = [
    tuple(map(int,input().split()))
    for _ in range(2)
]

# 좌표평면을 표현한 2차원 배열
checked = [
    [0] * (MAX_R + 1)
    for _ in range(MAX_R + 1)
]

# 좌표평면에서 직사각형을 체크
for i, (x1,y1,x2,y2) in enumerate(rects, start = 1) :
    x1,y1 = x1 + OFFSET, y1 + OFFSET
    x2,y2 = x2 + OFFSET, y2 + OFFSET

    for x in range(x1,x2) :
        for y in range(y1,y2) :
            checked[x][y] = i

# 1, 2 순으로 붙였는데도 
#숫자 1로 남아있는 곳들 중 최대최소 x,y값을 전부 계산
min_x, max_x, min_y, max_y = MAX_R,0,MAX_R,0

first_rect_exist = False

for x in range(MAX_R + 1) :
    for y in range(MAX_R + 1) :
        if checked[x][y] == 1 :
            first_rect_exist = True
            min_x = min(min_x,x)
            max_x = max(max_x,x)
            min_y = min(min_y,y)
            max_y = max(max_y,y)
    
# 첫번째 직사각형이 전혀 남아있지 않다면 넓이는 0
if not first_rect_exist :
    area = 0

else :
    area = (max_x - min_x + 1) * (max_y - min_y + 1)

print(area)