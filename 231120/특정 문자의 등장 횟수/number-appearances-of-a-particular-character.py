string = input()

cnt1 = 0
cnt2 = 0

for i in range(len(string)-1) :
    if string[i] == 'e' and string[i+ 1] =='e' :
        cnt1 += 1
    if string[i] == 'e' and string[i+1] =='b' :
        cnt2 += 1

print(cnt1, cnt2)