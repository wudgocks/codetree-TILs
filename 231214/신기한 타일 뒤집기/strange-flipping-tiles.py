MAX_R = 10000
OFFSET = 5000
n = int(input())

checker = [0] * (MAX_R + 1)

point = OFFSET
for _ in range(n) :
    x,d = tuple(input().split())
    x = int(x)
    if d =='R' :
        for i in range(point, point + x) :
            checker[i] = 1
        point += x-1

    if d =='L' :
        for i in range(point-1,point-x-1,-1) :
            checker[i] = 2
        point -= x-1

black = 0
white = 0

for element in checker :
    if element == 2 :
        white += 1
    if element == 1 :
        black += 1

print(white,black)