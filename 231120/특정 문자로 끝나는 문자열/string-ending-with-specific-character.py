lst = []
for _ in range(10) :
    string = input()
    lst.append(string)

one = input()
checker = 0
for string in lst :
    if string[len(string)-1] == one :
        print(string)
        checker += 1

if checker == 0 :
    print('None')