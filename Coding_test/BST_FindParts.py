#
# 부품 찾기
# N개의 부품이 존재
# M개의 부품이 존재하는지 확인
# N, M은 정수
# N개의 부품 중, M개의 부품이 있는지 yes,no로 확인
#

N = 5 #int(input("N: "))
total_list = [8, 3, 7, 9, 2] #list(map(int, input("Total: ").split()))

M = 3 #int(input("M: "))
find_list = [6, 7, 9] #list(map(int, input("Find: ").split()))


def search_list(lists, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    if lists[mid] == target:
        return True
    elif target < lists[mid]:
        return search_list(total_list, target, start, mid-1)
    else:
        return search_list(total_list, target, mid+1, end)

def search2_list(lists, target, start, end):
    while start <=  end:
        mid = (start + end) // 2
        if target == lists[mid]:
            return True
        elif target < lists[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return None

total_list.sort()
for i in find_list:
    result = search_list(total_list, i, 0, N-1)
    if result != None:
        print("yes", end=" ")
    else:
        print("no", end=' ')

print("\n")
print(N, total_list)
print(M, find_list)

