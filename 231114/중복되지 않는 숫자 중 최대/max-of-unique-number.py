import sys

n = int(input())

lst = list(map(int,input().split()))
counting = [0] * 1001

newLst = []

for element in lst :
    counting[element] += 1

for i in range(len(counting)) :
    if counting[i] == 1 :
        newLst.append(i)

maxVal = -sys.maxsize

for element in newLst :
    if element > maxVal :
        maxVal = element

if maxVal == -sys.maxsize :
    print(-1)
else :
    print(maxVal)