#
# 부품 찾기
# N개의 부품이 존재
# M개의 부품이 존재하는지 확인
# N, M은 정수
# N개의 부품 중, M개의 부품이 있는지 yes,no로 확인
#

N = 5 #int(input("N: "))
#total_list = set(map(int, input("total: ").split()))
total_list = set([8, 3, 7 ,9, 2])

M = 3 #int(input("M: "))
find_list = [6, 7, 9] #list(map(int, input("Find: ").split()))

for i in find_list:
    if i in total_list:
        print("yes", end=" ")
    else:
        print("no", end=' ')


