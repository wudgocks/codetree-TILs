n = int(input())

# 배열 입력
lst = [
    int(input())
    for _ in range(n)
]

for i in range(len(lst)) :
    if lst[i] >= 0 :
        lst[i] = 0
    else :
        lst[i] = 1
minus = 0
plus = 0
for elem in lst :
    if elem == 0 :
        plus +=1
    else :
        minus += 1

print(max(minus,plus))