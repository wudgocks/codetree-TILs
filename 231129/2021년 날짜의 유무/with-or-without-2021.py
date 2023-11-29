M,D = map(int,input().split())

def dateChecker(M,D) :
    # day_31 = [1,3,5,7,8,10,12]
    day_30 = [4,6,9,11]
    
    if M > 12 :
        return False
    if D > 31 :
        return False
    if M in day_30 :
        if D > 30 :
            return False
    if M == 2 :
        if D > 28 :
            return False
   
    return True

if dateChecker(M,D) :
    print("Yes")
else :
    print("No")