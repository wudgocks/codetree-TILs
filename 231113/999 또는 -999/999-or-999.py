import sys

maxVal = -sys.maxsize
minVal = sys.maxsize

lst = list(map(int,input().split()))

for element in lst :
    if element != 999 and element > maxVal :
        maxVal = element
    if element != - 999 and element < minVal :
        minVal = element

print(maxVal,minVal)