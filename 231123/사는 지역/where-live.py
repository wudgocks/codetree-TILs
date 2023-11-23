class Local :
    def __init__ (self,name, addr, city) -> None :
        self.name = name
        self.addr = addr
        self.city = city

n = int(input())
local_info = []

for _ in range(n) :
    name,addr, city = tuple(input().split())
    local_info.append(Local(name,addr,city))

arr = [person.name for person in local_info]
arr.sort()

for i in range(n) :
    if local_info[i].name == arr[n-1] :
        print('name',local_info[n-1].name)
        print('addr',local_info[n-1].addr)
        print('city', local_info[n-1].city)