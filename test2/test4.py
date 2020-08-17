from itertools import permutations
numbers = "011"
num = []
for i in range(len(numbers)):
    test = list(set(permutations(numbers)))
    print(test)
for i in range(len(numbers)):
    print(i)
