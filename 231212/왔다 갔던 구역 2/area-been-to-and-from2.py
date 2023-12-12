OFFSET = 100
MAX_R = 200

n = int(input())
checker = [0] * (MAX_R + 1)

point = OFFSET
for i in range(n) :
    x,d = map(str,input().split())
    x = int(x)
    if d == 'R' :
        for p in range(point,point + x) :
            checker[p] += 1
        point+= x

    if d == 'L' :
        for p in range(point,point-x,-1) :
            checker[p] += 1
        point -= x

leng = 0
for element in checker :
    if element >= 2 :
        leng += 1

print(leng)