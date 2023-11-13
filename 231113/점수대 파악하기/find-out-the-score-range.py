score_lst = list(map(int,input().split()))

score_range = [0] * 11 # 100 부터 10까지 이므로

for element in score_lst :
    if element == 0 : 
        break
    score_range[element// 10] += 1

for i in range(len(score_range)-1, 0 ,-1) :
    print(f'{i*10} - {score_range[i]}')