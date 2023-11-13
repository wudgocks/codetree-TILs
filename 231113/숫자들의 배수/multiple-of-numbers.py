n = int(input())
lst = []
cnt = 0

for i in range(1,10 + 1) :
    lst.append(n*i)

for elem in lst :
    if cnt == 2 :
        break
    if elem % 5 == 0 :
        cnt += 1
    print(elem, end = " ")