string1 = input()
string2 = input()

len_1 = len(string1)
len_2 = len(string2)

while True :
    idx = -1

    candidates = len_1 - len_2 + 1
    for i in range(candidates) :
        is_same = True

        for j in range(len_2) :
            if string1[i + j] != string2[j] :
                is_same = False
                break
        
        if is_same :
            idx = i
            break
    
    if idx == -1 :
        break
    
    string1 = string1[:idx] + string1[idx + len_2 :]

    len_1 = len(string1)

print(string1)