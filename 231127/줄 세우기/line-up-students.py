class Students :
    def __init__ (self,height,weight,num) :
        self.height = height
        self.weight = weight
        self.num = num

n = int(input())
students = []

for i in range(n) :
    height, weight = tuple(input().split())

    students.append(Students(int(height),int(weight),i+1))

students.sort(key = lambda x : (-x.height, -x.weight, x.num))

for student in students :
    print(student.height,student.weight,student.num)