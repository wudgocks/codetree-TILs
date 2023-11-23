class _007 :
    def __init__(self, secretCode, meetingPoint, time) :
        self.secretCode = secretCode
        self.meetingPoint = meetingPoint
        self.time = time

s_code, m_point, time = tuple(input().split())

instance = _007(s_code,m_point, int(time))
print('secret code :', instance.secretCode)
print('meeting point :', instance.meetingPoint)
print('time :', instance.time)