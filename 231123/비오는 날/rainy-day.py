class Forcast :
    def __init__ (self,date,day,weather) :
        self.date = date
        self.day = day
        self.weather = weather

n = int(input())

forcast_info = []

for _ in range(n) :
    date, day, weather = tuple(input().split())
    forcast_info.append(Forcast(date,day, weather))

arr = [w.weather for w in forcast_info]
arr.sort()
for i in range(n) :
    if forcast_info[i].weather == 'Rain' :
        print(forcast_info[i].date, forcast_info[i].day, forcast_info[i].weather)
        break