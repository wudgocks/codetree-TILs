# 수열 : 전항 + 전전항 *2
a1,a2 = map(int,input().split())

lst = [a1, a2]

for i in range(3, 10 + 1) :
    lst.append(lst[-1] + 2 * lst[-2])
    
for element in lst :
    print(element, end = " ")