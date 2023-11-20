n = int(input())
str_lst = []
sum_len = 0
counter = 0
for i in range(n) :
    string = input()

    str_lst.append(string)

char =input()

for string in str_lst :
    if string[0] == char :
        sum_len += len(string)
        counter += 1

try :
    print(f'{counter} {sum_len/counter:.2f}')

except ZeroDivisionError :
    print(f'{counter} -nan')