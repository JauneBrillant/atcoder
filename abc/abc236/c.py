n, m = map(int, input().split())
s = list(input().split())
t = list(input().split())

j = 0
for i in range(n):
    if s[i] == t[j]:
        print("Yes")
        j += 1
    else:
        print("No")
