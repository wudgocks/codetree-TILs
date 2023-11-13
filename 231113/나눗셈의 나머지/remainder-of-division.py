a,b = map(int,input().split())

remain = []
counter = [0] * 10 # 각 나머지가 나온 횟수를 저장할 카운터 리스트

for i in range(10) :
    if a//b == 0 :
        remain.append(a%b)
        break
    remain.append(a%b)
    a = a//b

for element in remain :
    counter[element] += 1

sumVal = 0

for element in counter :
    sumVal += element**2

print(sumVal)