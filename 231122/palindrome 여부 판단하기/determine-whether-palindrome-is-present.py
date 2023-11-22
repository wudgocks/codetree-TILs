def check_palindrome(string) :
    reverstring = ''
    for c in string :
        reverstring += c
    
    if string == reverstring :
        print("Yes")
    else :
        print("No")

_str = input()

check_palindrome(_str)