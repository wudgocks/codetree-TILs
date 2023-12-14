n = int(input())
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
x,y = 0,0 # 현재위치

for _ in range(n) :
    d, dir_num = tuple(input().split())
    dir_num = int(dir_num)
    if d == 'N' :
        y += dir_num
    if d == 'W' :
        x -= dir_num
    if d == 'S' :
        y -= dir_num
    if d == 'E' :
        x += dir_num

print(x,y)