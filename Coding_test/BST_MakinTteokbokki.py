#
# 떡볶기 떡 만들기
# line1, N : 떡의 개수, M : 떡의 길이 ( 1 <= N <= 1,000,000, 1 <= M <= 2,000,000,000
# line2, 개별 떡볶이 높이의 총합 >= M
# 적어도 M만큼의 떡을 집에 가져가기 위한 절단기 설정의 높이 최댓값을 출력한다.
#

n, m = 6, 6 # map(int, input().split())
tteok = [ 19, 15, 10, 17, 12, 20 ] # list(map(int, input().split()))

def BST(lists, target ):
    start = 0
    max_t = max(lists)
    while start <= max_t:
        sum_t = 0
        mid = (start + max_t) // 2
        for i in lists:
            if i > mid:
                sum_t += i - mid
        #print(sum_t)

        if  sum_t < target:
            #print("-1",mid)
            max_t = mid - 1

        else:
            #print("+1",mid)
            result = mid
            start = mid + 1

    return result
result = BST(tteok, m, )
print(result)
