import sys
maxVal1 = -sys.maxsize
maxVal2 = -sys.maxsize
n = int(input())

lst = list(map(int,input().split()))

for element in lst :
    if element > maxVal1 :
        maxVal1 = element

for element in lst :
    if element != maxVal1 and element > maxVal2 :
        maxVal2 = element
    
print(maxVal1, maxVal2)