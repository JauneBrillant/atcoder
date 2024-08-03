from collections import defaultdict

n, q = map(int, input().split())

graph = defaultdict(set)
for _ in range(q):
    t, a, b = map(int, input().split())
    match t:
        case 1:
            graph[a].add(b)
        case 2:
            if b in graph[a]:
                graph[a].remove(b)
        case 3:
            print("Yes" if b in graph[a] and a in graph[b] else "No")
