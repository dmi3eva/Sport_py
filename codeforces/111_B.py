def count_blocks(line):
    current = line[0]
    blocks = 1
    for _symbol in line:
        if _symbol != current:
            blocks += 1
            current = _symbol
    return blocks


n = int(input())
for _ in range(n):
    n, a, b = map(int, input().split())
    line = input()
    if b > 0:
        answer = n * (a + b)
    else:
        answer = a * n + b * (1 + count_blocks(line) // 2)
    print(str(answer))

