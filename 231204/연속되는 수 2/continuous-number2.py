n = int(input())

lst = []
arr = []
counterLst = []

for i in range(n) :
    num = int(input())
    lst.append(num)

counter = 1
for i in range(len(lst)) :
    # 값이 달라지면 checker = 1
    if lst[i-1] == lst[i] :
        counter += 1
        counterLst.append(counter)
    else :
        counter = 1
        counterLst.append(counter)
        
print(max(counterLst))