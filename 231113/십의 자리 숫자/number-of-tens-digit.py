lst = list(map(int,input().split()))
counting = [0] * 10
ten_lst = []
for i in range(len(lst)) :
    if lst[i] == 0 :
        break
    ten_lst.append(lst[i]//10)

for element in ten_lst :
    counting[element] += 1

for i in range(1, 10) :
    print(f'{i} - {counting[i]}')