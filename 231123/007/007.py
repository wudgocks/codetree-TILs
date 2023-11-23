class _007 :
    def __init__(self, secretCode, meetingPoint, time) :
        self.secretCode = secretCode
        self.meetingPoint = meetingPoint
        self.time = time
arr = list(map(str,input().split()))
arr[2] = int(arr[2])
instance = _007(arr[0],arr[1],arr[2])
print('secret code :', instance.secretCode)
print('meeting point :', instance.meetingPoint)
print('time :', instance.time)