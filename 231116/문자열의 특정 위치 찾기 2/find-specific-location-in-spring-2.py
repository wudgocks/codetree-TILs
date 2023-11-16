str_lst = ["apple", "banana", "grape", "blueberry", "orange"]

c = input()
counter = 0
for i in range(len(str_lst)) :
    if str_lst[i][3] == c or str_lst[i][2] == c :
        print(str_lst[i])
        counter += 1

print(counter)