n = int(input())

# 배열 입력
lst = [
    int(input())
    for _ in range(n)
]

ans,cnt = 0,0
for i in range(len(lst)) :
    if lst[i] >= 0 :
        lst[i] = 0
    else :
        lst[i] = 1

counter = 1
for i in range(len(lst)) :
    if i == 0 or lst[i] != lst[i-1] :
        counter = 1

    else :
        counter += 1

    ans = max(ans,counter)

print(ans)