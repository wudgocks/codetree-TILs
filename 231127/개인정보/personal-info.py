class PersonInfo :
    def __init__ (self,name,height,weight) :
        self.name,self.height,self.weight = name,height,weight

people = []

for _ in range(5) :
    name,height,weight = tuple(input().split())
    people.append(PersonInfo(name,int(height),float(weight)))

people.sort(key = lambda x : x.name)

print("name")
for person in people :
    print(person.name,person.height,person.weight)

people.sort(key = lambda x : -x.height)

print()
print("height")
for person in people :
    print(person.name,person.height,person.weight)