def alpa(string) :
    string = list(string)
    counter = 0
    for i in range(len(string)) :
        for j in range(i) :
            if string[j] != string[i] :
                counter += 1
    if counter == 0 :
        print("No")
    else :
        print('Yes')
s = input()

alpa(s)