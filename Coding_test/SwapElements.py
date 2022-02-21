# 두 배열의 원소 교체
#
#  A, B 두 배열은 N개의 원소로 구성(자연수)
# K번의 원소 교체 가능
# A의 모든 원소의 합이 최대값이 되길 원함
# N과 K가 주어졌을때, A의 최대값은?
#

N, K = 5, 3#map(int, input().split())
A =  [1, 2, 5, 4, 3]#list(map(int, input().split()))
B =  [5, 5, 6, 6, 5]#list(map(int, input().split()))

A.sort()
B.sort(reverse=True)
for i in range(K):
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]
    else:
        break
print(sum(A))
