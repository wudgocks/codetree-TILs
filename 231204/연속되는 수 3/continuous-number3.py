n = int(input())

# 배열 입력
lst = [
    int(input())
    for _ in range(n)
]

counterLst = []

for i in range(len(lst)) :
    if lst[i] >= 0 :
        lst[i] = 0
    else :
        lst[i] = 1

counter = 1
for i in range(len(lst)) :
    if i == 0 or lst[i] != lst[i-1] :
        counter = 1
        counterLst.append(counter)
    else :
        counter += 1
        counterLst.append(counter)
        
print(max(counterLst))