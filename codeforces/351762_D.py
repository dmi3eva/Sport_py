def get_disposal(n, towers):
    towers.sort()
    size = len(towers)
    half = (size + 1) // 2
    happy_disposal = [towers[half + i // 2] if i % 2 else towers[i // 2] for i in range(size)]
    happy_disposal_str = list(map(str, happy_disposal))
    return " ".join(happy_disposal_str)


t = int(input())
for _ in range(t):
    n = int(input())
    towers = list(map(int, input().strip().split()))
    print(get_disposal(n, towers))