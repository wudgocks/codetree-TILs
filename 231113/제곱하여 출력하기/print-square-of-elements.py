n = int(input())
lst = list(map(int,input().split()))

new_lst = [elem ** 2 for elem in lst]

for i in range(len(new_lst)) :
    print(new_lst[i], end = " ")