#
# 행(N)을 선택후, 열(M)에서 가장 낮은 숫자를 뽑아야함
# 여러 행중 가장 높은 숫자를 뽑아야 함
#

n,m = map(int, input().split())
list = [list(map(int,input().split())) for i in range(n) ]

for i in range(n):
   list[i] = sorted(list[i])
print(max(max(list)))
