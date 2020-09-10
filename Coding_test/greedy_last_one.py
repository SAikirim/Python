#
# 1이 될 때까지
#
# 1. N에서 1을 뺀다
# 2. N을 K로 나눈다.(단 N은 K로 나누어 떨어짐)
# 위 2가지 방법을 사용하여 N을 1로 만드는 최소 횟수를 구하라

n, k = map(int, input().split())

num = 0
while n != 1 :
    if n % k == 1:
        n -= 1
        num +=1
    n //= k
    num += 1


print(num)
