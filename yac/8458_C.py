n = int(input())
last_value = None

for _ in range(n):
    value = int(input())
    if value != last_value:
        print(value)
    last_value = value