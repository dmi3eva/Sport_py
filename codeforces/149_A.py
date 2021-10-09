n = int(input())
a = list(map(int, input().strip().split()))
a.sort(reverse=True)
if (sum(a) < n):
    print(-1)
else:
    k = 0
    height = 0
    while height < n:
        height += a[k]
        k += 1
    print(k)

