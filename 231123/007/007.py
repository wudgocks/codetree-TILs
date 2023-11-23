class _007 :
    def __init__(self, secretCode, meetingPoint, time) :
        self.secretCode = secretCode
        self.meetingPoint = meetingPoint
        self.time = time

instance = _007('codetree', 'L', 13)
print('secret code :', instance.secretCode)
print('meeting point :', instance.meetingPoint)
print('time :', instance.time)