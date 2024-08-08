N, M = map(int, input().split())
C = []
for _ in range(M):
    _ = int(input())
    a = set(map(int, input().split()))
    C.append(a)
correct = set([x for x in range(1, N + 1)])
    
ans = 0
for bit in range(1 << M):
    st = set()
    for i in range(M):
        if bit & (1 << i):
            st |= C[i]
    
    if st == correct:
        ans += 1

print(ans)
