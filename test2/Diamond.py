line = int(input("Diamond 의 길이를 입력하세요(2~30) : "))
#line = 5

for i in range(1, line+1):
    print(" " * (line-i) + "*"*(2*i-1))
for j in range (line-1, 0, -1):
    print(" " * (line-j) + "*"*(j*2-1))


print()
print("="*(line*2 - 1))
for i in range(line):
    print(" "*(i)+"*" * (line*2-i*2-1))
for j in range(1,line):
    print(" "*(line-j-1)+"*" * ((j)*2+1))
print("="*(line*2 - 1))
