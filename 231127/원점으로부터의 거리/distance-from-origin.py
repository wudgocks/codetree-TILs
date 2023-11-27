class Distance :
    def __init__ (self,x,y,m,idx) :
        self.x = x
        self.y = y
        self.m = m
        self.idx = idx

n = int(input())
points = []
Manhattan = []

# 원점에서 가까운 점부터 번호를 출력해라
for i in range(n) :
    x,y = tuple(input().split())
    points.append(Distance(int(x),int(y), 0, i + 1))
   
for i in range(n) :
    manhattan = abs(points[i].x) + abs(points[i].y)
    points[i].m = manhattan   

points.sort(key = lambda x : (x.m, x.idx))

for point in points :
    print(point.idx)