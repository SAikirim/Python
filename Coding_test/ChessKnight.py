#
# 왕실의 나이트
# 나이트의 위치가 주어졌을때, 나이트가 이동할 수 있는 경우의 수
#

location = input()
x = location[0]
y = location[1]

row = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
column = [ '1', '2', '3', '4', '5', '6', '7', '8']
steps = [(-2,-1), (-1, -2), (1,-2), (2,-1), (2,1), (1,2), (-1,2), (-2,1)]

count = 0
for step in steps:
    if 0 <= row.index(x)+(step[0]) < 8:
        if 0 <= column.index(y)+(step[1]) < 8:
            count += 1

print(count)
