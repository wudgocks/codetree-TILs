sym_arr = []
tem_arr = []

menual = []
counter = [0] * 4

for i in range(3) :
    sym, tem = input().split()
    sym_arr.append(sym)
    tem = int(tem)
    tem_arr.append(tem)

# 진료소로 가는 사람 체크
for i in range(3) :
    if sym_arr[i] == 'Y' and tem_arr[i] >= 37 :
        menual.append('A')
    elif sym_arr[i] == 'N' and tem_arr[i] >= 37 :
        menual.append('B')
    elif sym_arr[i] =='Y' and tem_arr[i] < 37 :
        menual.append('C')
    else :
        menual.append('D')

# 진료소로 간 사람 수 체크
for element in menual :
    if element == 'A' :
        counter[0] += 1
    elif element == 'B' :
        counter[1] += 1
    elif element == 'C' :
        counter[2] += 1
    else :
        counter[3] += 1

for element in counter :
    print(element, end = " ")

if counter[0] >= 2 :
    print('E')