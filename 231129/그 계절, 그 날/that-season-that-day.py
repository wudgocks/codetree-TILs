Y,M,D = map(int,input().split())

# 윤년 여부 판단 
def is_leap(Y) :
    if Y % 4 == 0 :
        if (Y%400 != 0) and (Y%100 == 0) :
            return True 
        else :
            return False
    else :
        return False

# 날짜 존재 여부 판단
def is_or_not(Y,M,D) :
    day_30 = [4,6,9,11]
    if (is_leap(Y)) == True :
        if M == 2 :
            if D > 28 :
                return -1
        if M > 12 :
            return -1
        if D > 31 :
            return -1
        if M in day_30 :
            if D > 30 :
                return -1
        return 0
    
    else : # leap
        if M == 2 :
            if D > 29 :
                return -1
            else :
                return 0
        if M > 12 :
            return -1
        if D > 31 :
            return -1
        if M in day_30 :
            if D > 30 :
                return -1
        return 0
    

def thatSeason (Y,M,D) :
    if is_or_not(Y,M,D) == 0 :
        if M >= 3 and M <= 5 :
            print("Spring")
        elif M >= 6 and M <= 8 :
            print('Summer')
        elif M >= 9 and M <= 11 :
            print("Fall")
        else :
            print("Winter")
    else :
        print(-1)

thatSeason(Y,M,D)