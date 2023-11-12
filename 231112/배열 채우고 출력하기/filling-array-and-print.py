''' 리스트 슬라이싱 이용 '''
# lst = input().split()
# reversed_lst = lst[::-1]

# for i in reversed_lst :
#     print(i, end ="") 

''' for 역순 출력 이용 '''
lst = input().split()

for i in range(len(lst) -1,-1,-1) :
    print(lst[i], end = "")