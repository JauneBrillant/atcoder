from itertools import combinations

n, m = map(int, input().split())
ss = []
for _ in range(n):
    ss.append(input())

ans = n
for i in range(1, n + 1):
    for subset in combinations(range(n), i):
        st = set()
        for idx in subset:
            for j, c in enumerate(ss[idx]):
                if c == "o":
                    st.add(j)
        if len(st) == m:
            ans = min(ans, len(subset))

print(ans)
