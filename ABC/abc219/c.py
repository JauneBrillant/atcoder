x = input()
n = int(input())

hashmap = {}
for i, c in enumerate(x):
    hashmap[c] = chr(ord("a") + i)


ans = {}
for i in range(n):
    s = input()
    sort_s = ""
    for c in s:
        sort_s += hashmap[c]
    ans[sort_s] = s

sorted_key = sorted(ans.keys())
for key in sorted_key:
    print(ans[key])
