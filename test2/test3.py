'''
#
# 짝 정하기
# https://www.acmicpc.net/problem/2599
# 총 성별의 학생 수 : 정수 N (3≤N≤100,000)
# 모든 학생수 0 이상
'''
man = 6
reslut = [0, 0], [0,0], [0, 0]
num=[4,2], [1, 3], [1, 1]
print(0/1)
for i in range(3):
    if num[i][0] == num[i][1] + num[2-(i%1)][1]:
        reslut[i][0] = num[1][1]
        reslut[i][1] = num[2][1]
        print(reslut, sep="\n")
    else:
        print(0)
        break
