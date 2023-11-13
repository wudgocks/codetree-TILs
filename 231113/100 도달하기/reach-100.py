n = int(input())
lst = [1, n]

for i in range(3,100) :
    number = lst[-1]+ lst[-2]
    lst.append(number)
    if number >= 100 :
        break

for element in lst :
    print(element, end = " ")