n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True) 

resurt = 0
while m != 0 :
  for j in range(k):
    resurt += data[0]
    m -= 1
  resurt += data[1]
  m -= 1

print(resurt)
