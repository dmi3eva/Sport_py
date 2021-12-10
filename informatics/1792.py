n = int(input())
values = list(map(int, input().strip().split()))


dp = []
longest = 1
previous_indices = []
best_ind = 0
for current in range(n):
    size = 1
    ind = current
    for last in range(current - 1, -1, -1):
        if values[current] > values[last] and size < dp[last] + 1:
            size = dp[last] + 1
            ind = last
    dp.append(size)
    previous_indices.append(ind)
    if size > longest:
        longest = size
        best_ind = current

current = best_ind
seq = []
while current != previous_indices[current]:
    seq.append(values[current])
    current = previous_indices[current]
seq.append(values[current])


result = ' '.join([str(_v) for _v in seq[::-1]])
print(result)
