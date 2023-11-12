''' 입력과 즉시에 출력 '''
# n = int(input())

# for i in range(n) :
#     a, b = map(int,input().split())
#     tmp = 1
#     for j in range(a, b + 1) :
#         tmp *= j
#     print(tmp)


'''입력을 배열에 저장해서 한번에 출력 '''
n = int(input())
answer_lst = []
for i in range(n) :
    a, b = map(int,input().split())
    tmp = 1
    for j in range(a, b + 1) :
        tmp *= j
    answer_lst.append(tmp)
    
for i in range(len(answer_lst)) :
    print(answer_lst[i])