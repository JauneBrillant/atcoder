from itertools import takewhile

s = input()
n = len(s)

cnt_head = len(list(takewhile(lambda c: c == "a", s)))
cnt_back = len(list(takewhile(lambda c: c == "a", reversed(s))))

ss = s[: n - cnt_back + cnt_head]
print("Yes" if ss == ss[::-1] else "No")
