n = int(input())

lst = list(map(int,input().split()))

reversed_lst = lst[::-1]

for element in reversed_lst :
    if element%2 == 0:
        print(element, end = " ")