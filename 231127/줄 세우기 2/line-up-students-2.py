class StudentInfo :
    def __init__ (self,height, weight,number) :
        self.height = height
        self.weight = weight
        self.number = number
n = int(input())

students = []

for i in range(n) :
    height,weight = tuple(input().split())
    students.append(StudentInfo(int(height),int(weight), i + 1))

students.sort(key = lambda x : (x.height, -x.weight))

for student in students :
    print(student.height, student.weight, student.number)