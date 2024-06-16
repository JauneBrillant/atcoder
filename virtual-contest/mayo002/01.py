from itertools import takewhile

n = int(input())
ctz = sum(1 for _ in takewhile(lambda x: x == "0", reversed(bin(n))))
print(ctz)
