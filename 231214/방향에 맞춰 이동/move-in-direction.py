n = int(input())
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
x,y = 0,0 # 현재위치

for _ in range(n) :
    d, dir_num = tuple(input().split())
    dir_num = int(dir_num)
    if d == 'N' :
        nx,ny = x + dx[dir_num], y + dy[dir_num]
        y += dir_num
    if d == 'W' :
        nx,ny = x + dx[dir_num], y + dy[dir_num]
        x -= dir_num
    if d == 'S' :
        nx,ny = x + dx[dir_num], y + dy[dir_num]
        y -= dir_num
    if d == 'E' :
        nx,ny = x + dx[dir_num], y + dy[dir_num]
        x += dir_num

print(x,y)