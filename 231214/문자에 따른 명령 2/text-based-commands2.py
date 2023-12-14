x,y = 0,0
command = input()

command_lst = list(command)

# dx,dy 정의
dx = [1,0,-1,0]
dy = [0,-1,0,1]

# 현재는 북쪽을 바라보고 있음
current_dir = 3

for i in range(len(command)) :
    if command_lst[i] == 'L' : # 반시계 방향으로 90도 회전
        current_dir = (current_dir -1 + 4) % 4
    
    if command_lst[i] == 'R' : # 시계방향으로 90도 회전
        current_dir = (current_dir + 1) % 4
    
    if command_lst[i] == 'F' :
        x += dx[current_dir]
        y += dy[current_dir]
    
    

print(x,y)