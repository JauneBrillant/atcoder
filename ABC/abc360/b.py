s, t = input().split()

for w in range(1, len(s)):
    for c in range(w):
        if s[c::w] == t:
            print("Yes")
            exit()

print("No")
