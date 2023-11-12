n = int(input())

grade_lst = list(map(float,input().split()))

gradeSum = 0

for element in grade_lst :
    gradeSum += element

avg = gradeSum/n
grade = ""

if avg >= 4.0 :
    grade = 'Perfect'
elif avg >= 3.0 :
    grade = 'Good'
else :
    grade = 'Poor'

print(f'{avg:.1f}')
print(grade)