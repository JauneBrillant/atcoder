n, a = map(int, input().split())
t = list(map(int, input().split()))

curr_time = 0
for arr_time in t:
    finish_time = max(curr_time, arr_time) + a
    print(finish_time)
    curr_time = finish_time
