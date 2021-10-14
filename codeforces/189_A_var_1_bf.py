n, a, b, c = map(int, input().strip().split())
a, b, c = sorted([a, b, c])
total_amount = 0
for a_amount in range(n // a, -1, -1):
    remaining_after_a = n - a * a_amount
    if a_amount + remaining_after_a // b <= total_amount:
        break
    for b_amount in range(remaining_after_a // b, -1, -1):
        remaining_after_b = remaining_after_a - b * b_amount
        if a_amount + b_amount + remaining_after_b // c <= total_amount:
            break
        if remaining_after_b % c == 0:
            c_amount = remaining_after_b // c
            total_amount = max(total_amount, a_amount + b_amount + c_amount)
print(total_amount)