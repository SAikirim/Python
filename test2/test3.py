'''
#
# 짝 정하기
# https://www.acmicpc.net/problem/2599
# 총 성별의 학생 수 : 정수 N (3≤N≤100,000)
# 모든 학생수 0 이상
'''
n = 6
arr = [4, 2], [1, 3], [1, 1]
#n = int(input("Total NUM: "))
#arr = [list(map(int, input().split())) for _ in range(3)]

for x in range(arr[0][0]):
    ax = arr[0][0]- x
    y = n - arr[2][0] - arr[2][1] - x
    by = arr[1][0] - y
    z = arr[0][1] - y
    cz = arr[2][0] - z

j = 0
for i  in arr:
    j += sum(i)

if (n == j/2) and (x >= 0) and (y >= 0) and (z >= 0) and  \
    (ax >= 0) & (by >= 0) and (cz >= 0):
    print(1)
    print(x, ax)
    print(y, by)
    print(z, cz)
else:
    print(0)
