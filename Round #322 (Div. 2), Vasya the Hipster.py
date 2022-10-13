a, b = map(int, input().split())
f = 0
n = 0
for i in range(max(a, b)):
    if min(a, b) > 0:
        f += 1
        a -= 1
        b -= 1
    else:
        n = max(a, b) // 2

print(f"{f} {n}")
