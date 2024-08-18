from collections import deque

N, M = map(int, input().split())
E = list(tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(M))
G = [[] for _ in range(N)]
for u, v in E:
    G[u].append(v)
    G[v].append(u)


def com(n):
    return n * (n - 1) // 2


ng_edges = 0
is_bipartite = True
colors = [-1] * N
for i in range(N):
    if colors[i] != -1:
        continue

    white_v_cnt, black_v_cnt = 0, 0
    q = deque([(i, 0)])
    colors[i] = 0

    while q:
        u, c = q.popleft()
        if c == 0:
            white_v_cnt += 1
        else:
            black_v_cnt += 1

        for v in G[u]:
            if colors[v] == c:
                is_bipartite = False
            if colors[v] == -1:
                colors[v] = not c
                q.append((v, not c))

    ng_edges += com(white_v_cnt) + com(black_v_cnt)

print(com(N) - M - ng_edges if is_bipartite else 0)
