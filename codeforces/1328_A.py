def count_steps(n, k):
    return 0 if a % b == 0 else b - (a % b)


req = int(input())
for _ in range(req):
    a, b = map(int, input().strip().split())
    print(count_steps(a, b))