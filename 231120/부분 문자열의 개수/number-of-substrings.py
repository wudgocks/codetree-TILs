string = input()
part = input()

cnt = 0

for i in range(len(string)-1) :
    if string[i] == part[0] and string[i+1] == part[1] :
        cnt +=1

print(cnt)