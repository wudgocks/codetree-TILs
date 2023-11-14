import sys

lst = list(map(int,input().split()))

lst_upper_500 = []
lst_lower_500 = []

# 리스트 분류
for i in range(len(lst)) :
    if lst[i] > 500 :
        lst_upper_500.append(lst[i])
    else :
        lst_lower_500.append(lst[i])

# 500미만의 수중 가장 큰수
max_lower_500 = -sys.maxsize

# 500초과의 수중 가장 작은 수
min_upper_500 = sys.maxsize

for element in lst_lower_500 :
    if element > max_lower_500 :
        max_lower_500 = element

for element in lst_upper_500 :
    if element < min_upper_500 :
        min_upper_500 = element

print(max_lower_500, min_upper_500)