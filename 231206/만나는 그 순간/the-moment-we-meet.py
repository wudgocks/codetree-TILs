n,m = map(int,input().split())

# d = 어떤 방향으로 이동했는지 R or L
# t = 몇초동안 이동했는지

A_distance = []
B_distance = []

dstA = 0
dstB = 0
totalA = 0
totalB = 0
# A의 이동
for i in range(n) :
    d,t = tuple(map(str,input().split()))
    t = int(t)
    if d == 'R' :
        counter = totalA
        for j in range(t) :
            counter +=1
            A_distance.append(counter)
            totalA = counter

        dstA += t
    if d == 'L' :
        counter = totalA
        for j in range(t) :
            counter -= 1
            A_distance.append(counter)
            totalA = counter

        dstA -= t

# B의 이동
for i in range(m) :
    d,t = tuple(map(str,input().split()))
    t = int(t)
    if d == 'R' :
        counter = totalB
        for j in range(t) :
            counter +=1
            B_distance.append(counter)
            totalB = counter

        dstB += t
    if d == 'L' :
        counter = totalB
        for j in range(t) :
            counter -= 1
            B_distance.append(counter)
            totalB = counter

        dstB -= t
i =0
notMatched = False
for elem1,elem2 in zip(A_distance,B_distance) :
    i += 1
    if elem1 == elem2 :
        print(i)
        notMatched = False
        break
    notMatched = True

if notMatched :
    print(-1)