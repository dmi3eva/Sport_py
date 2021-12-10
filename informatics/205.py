n = int(input())
values = list(map(int, input().strip().split()))

dp = []
longest = 1
for current in range(n):
    size = 1
    for last in range(current - 1, -1, -1):
        if values[current] > values[last] and size < dp[last] + 1:
            size = dp[last] + 1
    dp.append(size)
    if size > longest:
        longest = size

print(longest)