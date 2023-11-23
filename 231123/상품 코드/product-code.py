class product :
    def __init__ (self,name ='codetree',code = 50) :
        self.name = name
        self.code = code

name, code = tuple(input().split())

instance1 =product()
instance2 =product(name,int(code))

print(f'product {instance1.code} is {instance1.name}')
print(f'product {instance2.code} is {instance2.name}')