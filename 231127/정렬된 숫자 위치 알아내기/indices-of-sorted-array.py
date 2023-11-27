class SEQ :
    def __init__ (self,number,idx, new) :
        self.number = number
        self.idx = idx
        self.new = new

n = int(input())
arr_and_idx = []
newArr = []

number = list(map(int,input().split()))

for i in range(n) :
    arr_and_idx.append(SEQ(number[i], i+1, 0))

newArr = arr_and_idx.copy()

newArr.sort(key = lambda x : x.number)

for i in range(n) :
    newArr[i].new = i + 1

for i in range(len(arr_and_idx)) :
    print(arr_and_idx[i].new, end = " ")