n = int(input())
numbers = list(map(int,input().split()))

numbers.sort()

group_max = 0

for i in range(n) :
    group_sum = numbers[i] + numbers[2 *n -1 -i]
    if group_sum > group_max :
        group_max = group_sum

print(group_max)