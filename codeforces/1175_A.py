def count_steps(n, k):
    steps_num = 0
    while n > 0:
        while n % k == 0 and n > 0:
            n //= k
            steps_num += 1
        steps_num += n % k
        n -= n % k
    return steps_num


req = int(input())
for _ in range(req):
    n, k = map(int, input().strip().split())
    print(count_steps(n, k))