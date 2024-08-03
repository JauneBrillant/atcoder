N = int(input())
T = []
A = []
for _ in range(N):
    t, k, *a = map(int, input().split())
    a = [x - 1 for x in a]
    T.append(t)
    A.append(a)

skills = [False] * N
skills[N - 1] = True
ans = 0
for i in reversed(range(0, N)):
    if skills[i]:
        ans += T[i]
        for j in A[i]:
            skills[j] = True

print(ans)
