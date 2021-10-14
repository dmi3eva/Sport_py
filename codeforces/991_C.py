def count_vasya_eaten(n, k):
    eaten = 0
    while n > 0:
        eaten += min(k, n)
        n -= eaten
        n -= n // 10
    return eaten


n = int(input())
half = (n + 1) // 2
left = 0
right = n
while left < right:
    middle = (left + right) // 2
    eaten = count_vasya_eaten(n, middle)
    if eaten < half:
        left = middle + 1
    else:
        right = middle

print(left)
