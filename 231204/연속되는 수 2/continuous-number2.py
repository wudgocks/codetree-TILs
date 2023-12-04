n = int(input())

lst = []
arr = []
counterLst = []

for i in range(n) :
    num = int(input())
    lst.append(num)

counter = 1
for i in range(len(lst)) :
    if i ==0 or lst[i-1] != lst[i] :
        counter = 1
        counterLst.append(counter)
    else :
        counter += 1
        counterLst.append(counter)
        
print(max(counterLst))