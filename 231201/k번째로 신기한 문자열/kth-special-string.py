n,k,T = map(str,input().split())
n = int(n)
k = int(k)

wordLst = []
T_leng = len(T)

# 직접작성한 starts_with -- a가ㅠ로 시작하는지 확인
def starts_with (a,b) :
    if len(a) < len(b) :
        return False
    
    # b의 길이만큼 살펴보며, a와 문자열이 동일한지 확인
    return a[:len(b)] == b

# 파이썬의 startswith 함수 사용
'''
for i in range(n) :
    string = input()
    if string.startswith(T) :
        wordLst.append(string)
'''

for _ in range(n) :
    string = input()
    if starts_with(string, T) :
        wordLst.append(string)

wordLst.sort()

print(wordLst[k-1])