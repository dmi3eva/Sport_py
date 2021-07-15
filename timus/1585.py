n = int(input())
counts = {}
for _ in range(n):
    pinguin = input()
    counts[pinguin] = counts.get(pinguin, 0) + 1
leader = list(counts.keys())[0]
for _pinguin, _count in counts.items():
    if _count > counts[leader]:
        leader = _pinguin
print(leader)