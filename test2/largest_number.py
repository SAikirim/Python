#
# Largest Number
#
from functools import cmp_to_key

test = [3, 30, 34, 5, 9]
def comparator(a, b):
    t1 = a + b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2))

n = [str(x) for x in test]
n = sorted(n, key=cmp_to_key(comparator), reverse=True)
print(n)

a, b = 10, 10
print ((a > b) - (a < b))
