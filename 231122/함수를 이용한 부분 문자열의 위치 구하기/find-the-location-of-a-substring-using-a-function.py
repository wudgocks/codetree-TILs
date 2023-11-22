str1 = input()
str2 = input()

def index_str (str1,str2) :
    stringidx = 0
    if str2 in str1 :
        stringidx = str1.index(str2)
    
    return stringidx

print(index_str(str1,str2))