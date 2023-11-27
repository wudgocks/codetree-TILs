class Person :
    def __init__ (self,name,height,weight) :
        self.name = name
        self.height = height
        self.weight = weight

n = int(input())

people = []
for _ in range(n) :
    name,height,weight = tuple(input().split())
    people.append(Person(name,int(height), int(weight)))

# 키를 기준으로 정렬
people.sort(key = lambda x : (x.height, -x.weight))

for person in people :
    print(person.name, person.height, person.weight)