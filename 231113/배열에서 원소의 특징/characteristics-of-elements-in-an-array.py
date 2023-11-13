lst = list(map(int,input().split()))

for i in range(len(lst)) :
    if lst[i] % 3 == 0 :
        idx = i
        break

print(lst[idx-1])