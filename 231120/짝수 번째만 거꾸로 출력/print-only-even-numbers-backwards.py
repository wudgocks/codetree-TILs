string = input()
evenlst = []
for i in range(len(string)) :
    if i % 2 == 1 :
        evenlst.append(string[i])

for i in range(len(evenlst)-1, -1, -1) :
    print(evenlst[i],end = '')