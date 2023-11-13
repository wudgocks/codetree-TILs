n = int(input())

lst = list(map(int,input().split()))

new_lst = []


for i in range(len(lst)) :
    if lst[i] % 2 == 0 :
        new_lst.append(lst[i])

for i in range(len(new_lst)) :
    print(new_lst[i], end = " ")