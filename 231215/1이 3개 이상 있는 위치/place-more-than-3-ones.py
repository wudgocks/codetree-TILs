n = int(input())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

dxs = [0,1,0,-1]
dys = [1,0,-1,0]

# dx,dy에서 인접한 위치가 격자 안으로 들어오는지를 판단하는 in_range() 함수 작성
def in_range(x,y) :
    return 0 <= x and x < n and 0 <= y and y < n

def adjacent_cnt (x,y) :
    cnt = 0 
    for dx,dy in zip(dxs,dys) :
        nx,ny = x + dx, y + dy
        if in_range(nx,ny) and arr[nx][ny] == 1 :
            cnt += 1
    return cnt 

# 각 칸을 탐색
ans = 0

for i in range(n) :
    for j in range(n) :
        if adjacent_cnt(i,j) >= 3 :
            ans += 1

print(ans)