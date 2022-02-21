#
# 1로 만들기
# 정수 X가 가능한 연산 4가지
# 1. X가 5로 나누어 떨어지면, 5로 나눔
# 2. X가 3으로 나누어 떨어지면, 3으로 나눔
# 3. X가 2로 나누어 떨어지면, 2로  나눔
# 4. X에서 1을 뺀다
# 정수 X가 주어졌을때, 4개의 연산을 적절히 사용하여 1로 만든다.
# 이때 연산을 사용하는 횟수의 최소값을 출력
#

x = int(input("intX: "))

count = 0
while x != 1:
    if x % 5 == 0:
        x //= 5
        count += 1
        print("5: ",x)
    elif x % 3 == 0:
        x //= 3
        count += 1
        print("3: ",x)
    elif x % 2 == 0:
        x //= 2
        count += 1
        print("2: ",x)
    else:
        x -= 1
        count += 1
        print("1: ",x)
print(count)
