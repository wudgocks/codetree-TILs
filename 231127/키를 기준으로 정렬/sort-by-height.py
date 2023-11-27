class Person :
    def __init__(self,name,cm,kg) :
        self.name = name
        self.cm = cm
        self.kg = kg

n = int(input())

people = []

for _ in range(n) :
    name,cm,kg = tuple(input().split())
    people.append(Person(name,cm,kg))

people.sort(key = lambda x : x.cm) # 키를 기준으로 정렬

for person in people :
    print(person.name,person.cm, person.kg)