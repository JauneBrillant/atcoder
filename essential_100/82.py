from datetime import datetime

while True:
    N = int(input())
    if N == 0:
        break

    schedules = []
    for _ in range(N):
        dep, arr = input().split()
        dep = datetime.strptime(dep, "%H:%M:%S").time()
        arr = datetime.strptime(arr, "%H:%M:%S").time()
        schedules.append((dep, 1))
        schedules.append((arr, -1))

    schedules.sort()

    need_train = 0
    ans = 0
    for _, type in schedules:
        need_train += type
        ans = max(ans, need_train)

    print(ans)
