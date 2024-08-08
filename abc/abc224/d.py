from collections import deque

M = int(input())
G = [[] for _ in range(10)]
for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

p = list(map(int, input().split()))
zero_v = next(num for num in range(1, 10) if num not in p)

state = {}
for i in range(8):
    state[p[i]] = i + 1
state[zero_v] = 0

initial_state = tuple(state[i] for i in range(1, 10))
deq = deque([(zero_v, initial_state, 0)])
seen = set([initial_state])

ans = -1
while deq:
    v, current_state, depth = deq.popleft()
    
    if current_state == (1, 2, 3, 4, 5, 6, 7, 8, 0):
        ans = depth
        break
    
    for nv in G[v]:
        new_state = list(current_state)
        new_state[v-1], new_state[nv-1] = new_state[nv-1], new_state[v-1]
        new_state = tuple(new_state)
        
        if new_state not in seen:
            seen.add(new_state)
            deq.append((nv, new_state, depth + 1))

print(ans)
