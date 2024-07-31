def nth_permutation(arr):
    import math

    rank = 1
    n = len(arr)
    factorial = math.factorial

    for i in range(n):
        smaller = 0
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                smaller += 1
        rank += smaller * factorial(n - i - 1)

    return rank


n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))


print(abs(nth_permutation(q) - nth_permutation(p)))
