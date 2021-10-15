def count_vasya_eaten(n, k):
    eaten = 0
    while n > 0:
        vasya = min(k, n)
        eaten += vasya
        n -= vasya
        n -= n // 10
    return eaten


n = int(input())
half = (n + 1) // 2
left = 1
right = n
while left < right:
    middle = (left + right) // 2
    eaten = count_vasya_eaten(n, middle)
    if eaten < half:
        left = middle + 1
    else:
        right = middle

print(left)
