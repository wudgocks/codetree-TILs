n = int(input())

arr_2d = [
    list(map(int,input().split()))
    for _ in range(n)
]
point = 0

def in_range(x,y) :
    return 0 <= x and x < n and 0 <= y and y < n

dxs = [0,1,0,-1]
dys = [1,0,-1,0]

for row in range(n) :
    for col in range(n) :
        cnt = 0
        for dx,dy in zip(dxs,dys) :
            nx = row + dx
            ny = col + dy

            if in_range(nx,ny) and arr_2d[nx][ny] == 1:
                cnt += 1
        
        if cnt >= 3:
            point += 1

print(point)