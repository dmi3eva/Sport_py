n, k = map(int, input().split())
a = map(int, input().split())
bum = 0
droid = 0
for ai in a:
    if ai > k:
        bum += ai - k
    if ai < k:
        droid += k - ai
print(f"{bum} {droid}")