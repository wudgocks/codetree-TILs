class Student :
    def __init__ (self,name,sub1,sub2,sub3) :
        self.name = name
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3

n = int(input())
students = []

for _ in range(n) :
    name,sub1,sub2,sub3 = tuple(input().split())
    students.append(Student(name,int(sub1),int(sub2),int(sub3)))

students.sort(key = lambda x : (x.sub1 + x.sub2 + x.sub3))

for student in students :
    print(student.name, student.sub1, student.sub2, student.sub3)