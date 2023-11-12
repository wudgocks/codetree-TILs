score_lst = [*map(float,input().split())]
sumVal = 0

for ele in score_lst :
    sumVal += ele

avg = sumVal/8

print(f'{avg:.1f}')