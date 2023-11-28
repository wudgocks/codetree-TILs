binaryNum = int(input())
num = 0
binaryArr = []

for i in str(binaryNum) :
    binaryArr.append(i)

for i in range(len(binaryArr)) :
    num = num * 2 + int(binaryArr[i])

num *= 17
digits = []

while True :
    if num < 2 :
        digits.append(num)
        break
    
    digits.append(num%2)
    num //= 2

for digit in digits[::-1] :
    print(digit, end = "")