class boom :
    def __init__ (self, code, color,second) :
        self.code = code
        self.color = color
        self.second = second

code, color, second = tuple(input().split())
instance = boom(code,color,int(second))

print('code :', instance.code)
print('color :', instance.color)
print('second :', instance.second)