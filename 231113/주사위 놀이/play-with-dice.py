# 던진 주사위를 저장하는 리스트
dice = list(map(int,input().split()))

counting = [0] * 7

for element in dice :
    counting[element] += 1

for i in range(1, len(counting)) :
    print(f'{i} - {counting[i]}')