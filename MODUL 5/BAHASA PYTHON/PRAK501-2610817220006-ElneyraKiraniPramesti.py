def MaxBilangan(a, b, c, d):
    max = a
    for x in (b, c, d):
        if x > max:
            max = x
    return max

a, b, c, d = map(int, input().split())
print(MaxBilangan(a, b, c, d))