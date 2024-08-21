N = int(input())
AB = list(tuple(map(int, input().split())) for _ in range(N))

events = []
for a, b in AB:
    events.append((a, -1))
    events.append((a + b, 1))
events.sort()

# ans[k] := k人がログインしていた日数
ans = [0] * (N + 1)
curr_login_number = 0
for i in range(len(events) - 1):
    day, t = events[i]
    if t == -1:
        curr_login_number += 1
    else:
        curr_login_number -= 1
    duration = events[i + 1][0] - day
    ans[curr_login_number] += duration

for i in range(1, N + 1):
    print(ans[i])
