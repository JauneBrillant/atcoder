n, m = map(int, input().split())
ss = [input() for _ in range(n)]

ans = n
for bit in range(1 << n):
    st = set()
    for i in range(n):
        if bit & (1 << i):
            for j, c in enumerate(ss[i]):
                if c == "o":
                    st.add(j)
    if len(st) == m:
        ans = min(ans, bin(bit).count("1"))

print(ans)
