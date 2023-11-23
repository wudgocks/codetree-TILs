class Forcast :
    def __init__ (self,date,day,weather) :
        self.date = date
        self.day = day
        self.weather = weather

n = int(input())
ans = Forcast('9999-99-99', '','')

for _ in range(n) :
    date, day, weather = tuple(input().split())

    f = Forcast(date,day,weather)

    if weather == 'Rain' :

        if ans.date >= f.date :
            ans = f

print(ans.date, ans.day, ans.weather)