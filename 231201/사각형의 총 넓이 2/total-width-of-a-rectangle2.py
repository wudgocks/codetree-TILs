OFFSET = 100

n = int(input())

area = [
    [0 for _ in range(201)]
    for _ in range(201)
]

for i in range(n) :
    x1,y1,x2,y2 = tuple(map(int,input().split()))
    x1 += OFFSET
    y1 += OFFSET
    x2 += OFFSET
    y2 += OFFSET
    
    for x in range(x1,x2) :
        for y in range(y1,y2) :
            area[x][y] = 1


w = 0

for x in range(200) :
    for y in range(200) :
        if area[x][y] == 1 :
            w += 1

print(w)