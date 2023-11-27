arr = list(map(int,input().split()))

a = arr[0]
b = arr[1]
c = arr[2]
d = arr[3]

hours,mins = a,b
elapsed_time = 0

while True :
    if hours == c and mins == d :
        break
    
    elapsed_time += 1
    mins += 1

    if mins == 60 :
        hours += 1
        mins = 0
    
print(elapsed_time)