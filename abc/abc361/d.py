from collections import deque

N = int(input())
S = input() + ".."
T = input() + ".."

q = deque([(S, 0)])
visited = set()
visited.add(S)

ans = -1
while q:
    s, depth = q.popleft()
    if s == T:
        ans = depth
        break

    a, b = next((i, i + 1) for i, c in enumerate(s) if c == ".")
    for i in range(N + 1):
        if "." not in s[i : i + 2]:
            t = list(s)
            t[i], t[a] = t[a], t[i]
            t[i + 1], t[b] = t[b], t[i + 1]
            t = "".join(t)
            if t not in visited:
                visited.add(t)
                q.append((t, depth + 1))

print(ans)
