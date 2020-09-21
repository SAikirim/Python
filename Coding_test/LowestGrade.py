#
# LowestGrade
#

n = int(input())
student = []
for i in range(n):
    data = input().split()
    student.append((data[0], data[1]))
A = sorted(student, key=student[1])

print(student)
