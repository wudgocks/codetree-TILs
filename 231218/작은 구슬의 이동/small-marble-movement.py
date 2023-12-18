# n = 격자의 크기, t = 시간
n, t = map(int,input().split()) 

arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

#  구슬의 정보
r,c,d = tuple(input().split())
r = int(r)
c = int(c)

dxs = [0,1,-1,0]
dys = [1,0,0,-1]

def in_range(x,y) :
    return 0 <= x and x < n and 0 <= y and y < n

mapper = {
    'R' : 0,
    'D' : 1,
    'U' : 2,
    'L' : 3
}

move_dir = mapper[d]

for i in range(t+1) :
    nx,ny = r + dxs[move_dir], c + dys[move_dir]
    if not in_range(nx,ny) :
        move_dir = 3 - move_dir
    
    r,c = r + dxs[move_dir], c + dys[move_dir]

print(r,c)