n = int(input())
lst = [1, n]

while True :
    number = lst[-1]+ lst[-2]
    lst.append(number)
    if number > 100 :
        break

for element in lst :
    print(element, end = " ")