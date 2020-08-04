nums = input("진짜 구술 수, 가짜 구술 수, 최대 사람 수 : ")
nums = nums.split(' ')

if ((0 < int(nums[0] or nums[1]) <= 1000000000) and (0 < int(nums[2]) <= 1000000)) :
    print("ok")
else:
    print("USAGE: [NUM] [NUM] [NUM](0 < NUM < 1000,000")


S=int(nums[0])
F=int(nums[1])
M=int(nums[2])

Max=0
for f in range(1, F+1):
    Max = S * f + Max

Max+=1
try:
    print("Max: " , Max)
    for m in range(M, 1, -1):
        print("m: " , m)
        p = Max%m
        print("p: " , p)
        if  0 == p:
            break
        else 1 == m:
            print("1")
    print(m)
except:
    print("-1")
