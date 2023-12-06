MAX_T = 1000000

n,m = map(int,input().split())
pos_a, pos_b = [0] * (MAX_T + 1), [0] * (MAX_T + 1)

# A가 매초마다 서있는 위치를 기록
time_a = 1
for _ in range(n) :
    v,t = tuple(map(int,input().split()))
    for _ in range(t) :
        pos_a[time_a] = pos_b[time_a -1] + v
        time_a += 1

# B가 매초마다 서있는 위치를 기록
time_a = 1
for _ in range(n) :
    v,t = tuple(map(int,input().split()))
    for _ in range(t) :
        pos_b[time_b] = pos_b[time_b -1] + v
        time_b += 1

# A와 B중 더 앞서 있는 경우를 확인
# A가 리더면 1, B가 리더면 2로 관리

leader, ans = 0,0

for i in range(1,time_a) :
    if pos_a[i] > pos_b[i] :

        if leader == 2:
            ans += 1
        
        leader = 1
    
    elif pos_a[i] < pos_b[i] :

        if leader == 1 :
            ans += 1
        
        leader = 2

print(ans)