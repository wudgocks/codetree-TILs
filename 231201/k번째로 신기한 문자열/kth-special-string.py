n,k,T = map(str,input().split())
n = int(n)
k = int(k)

wordLst = []
T_leng = len(T)

for i in range(n) :
    string = input()
    if string.startswith(T) :
        wordLst.append(string)

wordLst.sort()

print(wordLst[k-1])