'''
n = 배열 크기(수)
m = 더하는 개수
k = 연속해서 더할 수 있는 개수
가장 큰수들을 더해 최대값 구하기
가장 큰수는 연속해서 더하는데에 제한이 있음
'''

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)

'''
resurt = 0
while m != 0 :
  for j in range(k):
    resurt += data[0]
    m -= 1
  resurt += data[1]
  m -= 1

print(resurt)
'''
count = m//(k+1) * k
count += m %(k+1)

result = count * data[0]
result += (m - count) * data[1]

print(result)
