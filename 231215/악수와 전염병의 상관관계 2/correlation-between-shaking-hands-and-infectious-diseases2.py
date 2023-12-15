class Shake :
    def __init__(self,time,person1,person2) :
        self.time, self.person1,self.person2 = time,person1,person2


# n 명의 개발자, k번의 악수로 전염, 처음 전염병에 걸린 번호 P, t번 악수
n,k,p,T = map(int,input().split())
shakes = []

for _ in range(T) :
    time,person1,person2 = tuple(map(int,input().split()))
    shakes.append(Shake(time,person1,person2))

shake_num = [0] * (n + 1)
inflected = [False] * (n + 1)

inflected[p] = True

shakes.sort(key = lambda x : x.time)

for shake in shakes :
    target1 = shake.person1
    target2 = shake.person2

    if inflected[target1] :
        shake_num[target1] += 1
    if inflected[target2] :
        shake_num[target2] += 2
    
    if shake_num[target1] <= k and inflected[target1] :
        inflected[target2] = True
    
    if shake_num[target2] <= k and inflected[target2] :
        inflected[target1] = True

for i in range(1, n + 1) :
    if inflected[i] :
        print(1, end="")
    else :
        print(0, end="")