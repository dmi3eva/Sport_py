from math import sqrt, ceil

n = int(input())
for _ in range(n):
    number = int(input())
    print(str(int(ceil(sqrt(number)))))
