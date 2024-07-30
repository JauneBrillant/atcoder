N, M = map(int, input().split())
C = []
for _ in range(M):
    size = int(input())
    a = list(map(int, input().split()))
    C.append(a)

x = [i for i in range(1, N + 1)]
ans = 0
for bit in range(1 << M):
    st = set()
    for i in range(M):
        if bit & (1 << i):
            for e in C[i]:
                st.add(e)
    if sorted(st) == x:
        ans += 1

print(ans)
