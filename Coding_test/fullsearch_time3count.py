# time 3 count

n = int(input())
count = 0
for k in range(n+1):
    for i in range(60):
        for j in range(60):
            if '3' in str(k) + str(i) + str(j):
                count += 1
print(count)
