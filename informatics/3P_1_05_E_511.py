values = input().strip().split()
n, i, j = int(values[0]), int(values[1]), int(values[2])
i, j = min(i, j), max(i, j)
dist = min(j - i, n + i - j) - 1
print(dist)