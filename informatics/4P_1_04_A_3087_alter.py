

if __name__ == '__main__':
    n = int(input())
    bills = list(map(int, input().split()))
    s = int(input())
    inf = s + 1
    amounts = [0] + [inf] * s
    parents = [-1] * (s + 1)
    overall_min = inf
    for i in range(1, s + 1):
        for _b in bills:
            if i-_b >= 0 and amounts[i-_b] + 1 < amounts[i]:
                amounts[i] = amounts[i-_b] + 1
                parents[i] = _b
                if amounts[i] <= overall_min:
                    overall_min = amounts[i]
                    break

    if amounts[-1] == inf:
        print("No solution")
        exit(0)

    current = parents[-1]
    total = s
    while current != -1:
        print(current, end=' ')
        total -= current
        current = parents[total]




