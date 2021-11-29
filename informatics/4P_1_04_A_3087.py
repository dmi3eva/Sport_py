

if __name__ == '__main__':
    n = int(input())
    bills = list(map(int, input().split()))
    s = int(input())
    inf = s + 1
    amounts = [0]
    parents = [-1]
    for i in range(1, s + 1):
        amounts.append(inf)
        parents.append(-1)
        for _b in bills:
            if i-_b >= 0 and amounts[i-_b] + 1 < amounts[-1]:
                amounts[-1] = amounts[i-_b] + 1
                parents[-1] = _b

    if amounts[-1] == inf:
        print("No solution")
        exit(0)

    current = parents[-1]
    total = s
    while current != -1:
        print(current, end=' ')
        total -= current
        current = parents[total]




