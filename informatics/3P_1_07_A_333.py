a = int(input().strip())
b = int(input().strip())
for number in range(a, b + 1):
    if number % 2 == 0:
        print(number)