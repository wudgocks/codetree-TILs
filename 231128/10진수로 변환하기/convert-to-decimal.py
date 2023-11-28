binary = int(input())
num = 0

binaryArr = []

while (binary != 0) :
    binaryArr.append(binary%10)
    binary//=10

for i in range(len(binaryArr)-1,-1,-1) :
    num = num * 2 + binaryArr[i]

print(num)