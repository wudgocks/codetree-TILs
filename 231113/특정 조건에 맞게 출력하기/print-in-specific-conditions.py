# 홀수면 3더하고, 짝수면 2로 나눈 몫 출력
lst = list(map(int,input().split()))
newLst = []
for i in range(len(lst)) :
    if lst[i] == 0 :
        break
    if lst[i]%2 == 0 :
        newLst.append(lst[i]// 2)
    if lst[i]%2 == 1 :
        newLst.append(lst[i] + 3)

for element in newLst :
    print(element, end = " ")