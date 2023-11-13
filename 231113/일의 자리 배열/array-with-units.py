a,b = map(int,input().split())

lst = [a,b]

for i in range(3,11) :
    lst.append((lst[-1] + lst[-2])%10)

for i in range(len(lst)) :
    print(lst[i], end = " ")