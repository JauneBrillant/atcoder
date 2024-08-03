from collections import defaultdict

n = int(input())

hashmap = defaultdict(int)
for _ in range(n):
    s = input()

    if hashmap[s] == 0:
        print(s)
    else:
        print(s + "(" + str(hashmap[s]) + ")")
    hashmap[s] += 1
