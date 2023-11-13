''' 새로운 리스트 만들어서 뒤의 세개 구하기 '''
# lst = list(map(int,input().split()))
# new_arr = []

# for i in range(len(lst)) :
#     if lst[i] == 0 :
#         break
#     new_arr.append(lst[i])

# sumVal = 0

# for i in range(len(new_arr)-1, len(new_arr)-4, -1) :
#     sumVal += new_arr[i]

# print(sumVal)

''' arr[k-3], [k-2], [k-1] 구하기 '''

arr = list(map(int,input().split()))

for i in range (len(arr)) :
    if arr[i] == 0 :
        k = i # 0 이 나온 인덱스 구하기
        break

print(arr[k-3] + arr[k-2] + arr[k-1])