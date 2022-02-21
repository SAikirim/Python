#
# LowestGrade
#

#
# LowestGrade
#

n = int(input())
student = []
for i in range(n):
    data = input().split()
    student.append((data[0], int(data[1])))

student = sorted(student, key=lambda student: student[1])

for i in student:
    print(i[0], end=' ')
