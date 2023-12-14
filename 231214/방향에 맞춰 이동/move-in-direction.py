n = int(input())
x,y = 0,0 # 현재위치

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n) :
    d, dir_num = tuple(input().split())
    dir_num = int(dir_num)
    if d == 'E' :
        moving = 0
    if d == 'W' :
        moving = 1
    if d == 'S' :
        moving = 2
    if d == 'N' :
        moving = 3

    x += dx[moving] * dir_num
    y += dy[moving] * dir_num

print(x,y)