#
# 마법의 구슬
# https://www.acmicpc.net/problem/1095
#

nums = input("진짜 구술 수, 가짜 구술 수, 최대 사람 수 : ").split()

if not ((0 < int(nums[0] or nums[1]) <= 1000000000) and (0 < int(nums[2]) <= 1000000)) :
    print("USAGE: [NUM] [NUM] [NUM](0 < NUM < 1000,000")

S, F, M = map(int,nums)

# 최대 경우의 수 구하기
Max=0
for f in range(1, F+1):
    Max = S * f + Max

# 최대 사람 수 구하기
Max+=1
try:
    for m in range(M, 0, -1):
        p = Max%m
        if  0 == p:
            break
        elif 1== m :
            print("1")
    print(m)
except:
    print("-1")
