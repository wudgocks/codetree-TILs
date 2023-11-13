n = int(input())
lst = list(map(int,input().split()))

counting = [0] * 10

for element in lst :
    counting[element] += 1

for i in range(1, len(counting)) :
    print(counting[i])