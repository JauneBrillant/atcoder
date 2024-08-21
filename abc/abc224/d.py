from collections import deque

M = int(input())
G = [[] for _ in range(9)]
for _ in range(M):
    u, v = map(lambda x: int(x) - 1, input().split())
    G[u].append(v)
    G[v].append(u)
P = list(map(lambda x: int(x) - 1, input().split()))
empty = 36 - sum(P)
P += [empty]

ans = -1
que = deque([(P, 0)])
seen = set([tuple(P)])

while que:
    state, step = que.popleft()
    if state == [0, 1, 2, 3, 4, 5, 6, 7, 8]:
        ans = step
        break

    u = state[8]
    for v in G[u]:
        new_p = state[:]
        new_p[8], new_p[new_p.index(v)] = new_p[new_p.index(v)], new_p[8]
        if tuple(new_p) not in seen:
            seen.add(tuple(new_p))
            que.append((new_p, step + 1))

print(ans)
