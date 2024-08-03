n = int(input())
s = input()

ans = 0
for i in range(0, 10):
    for j in range(0, 10):
        for k in range(0, 10):
            a = s.find(str(i))
            b = s.find(str(j), a + 1)
            c = s.find(str(k), b + 1)
            if min(a, b, c) >= 0:
                ans += 1

print(ans)
