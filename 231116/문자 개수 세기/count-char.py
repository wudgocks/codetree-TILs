s = input()
c = input()

counter = 0
for i in range(len(s)) :
    if c == s[i] :
        counter +=1

print(counter)