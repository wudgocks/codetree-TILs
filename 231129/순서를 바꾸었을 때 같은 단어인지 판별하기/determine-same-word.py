str1 = input()
str2 = input()

if len(str1) != len(str2) :
    print("No")

else :
    strarr1 = list(str1)
    strarr2 = list(str2)
    strarr1.sort()
    strarr2.sort()

    jstr1 = ''.join(strarr1)
    jstr2 = ''.join(strarr2)

    if jstr1 == jstr2 :
        print("Yes")
    else :
        print("No")