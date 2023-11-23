class CodeName :
    def __init__ (self, code, score) :
        self.code = code
        self.score = score

code_name = []


for _ in range(5) :
    code, score = tuple(input().split())
    code_name.append(CodeName(code,int(score)))

minScore = 0
for i in range(1,5) :
    if code_name[minScore].score > code_name[i].score :
        minScore = i

print(code_name[minScore].code, code_name[minScore].score)