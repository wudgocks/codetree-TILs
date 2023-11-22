n = int(input())
str_lst = []

for i in range(n) :
    string = input()
    str_lst.append(string)

str_lst.sort()

for element in str_lst :
    print(element)