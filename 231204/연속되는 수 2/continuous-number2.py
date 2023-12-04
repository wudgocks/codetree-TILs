n = int(input())

lst = []
counter_lst = [1]

for i in range(n) :
    num = int(input())
    lst.append(num)

counter = 1

for i in range(len(lst)) :
    if lst[i] == lst[i-1] :
        counter += 1
    
    elif i == 0 or lst[i] != lst[i-1] :
        counter_lst.append(counter)
        counter = 1

print(max(counter_lst))