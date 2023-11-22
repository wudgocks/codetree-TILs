def check_palindrome(string) :
    reverstring = ''
    string = list(string)
    
    for i in range(len(string)-1, -1, -1) :
        reverstring += string[i]
    
    string = ''.join(string)
    
    if string == reverstring :
        print("Yes")
    else :
        print("No")
    
    
_str = input()

check_palindrome(_str)