class NextLevel :
    def __init__ (self, _id = "codetree", level = 10) :
        self._id = _id
        self.level = level

_id,level = tuple(input().split())

instance1 = NextLevel()
instance2 = NextLevel(_id,int(level))

print('user',instance1._id, 'lv', instance1.level)
print('user',instance2._id, 'lv', instance2.level)