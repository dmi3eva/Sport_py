n = int(input())
values = input().strip().split()
counter = 0
for ind, _value in enumerate(values):
    if ind > 0 and int(_value) > int(values[ind - 1]):
        counter += 1
print(counter)