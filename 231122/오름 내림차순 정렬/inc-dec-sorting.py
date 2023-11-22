n = int(input())
lst = list(map(int,input().split()))

lst.sort()
for element in lst :
    print(element, end = " ")
print()

lst.sort(reverse= True)
for element in lst :
    print(element, end = " ")