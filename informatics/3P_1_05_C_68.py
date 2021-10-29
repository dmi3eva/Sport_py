n = int(input())
values = input().strip().split()
counter = 0
for ind, _value in enumerate(values[1:-1]):
    if int(_value) > int(values[ind]) and int(_value) > int(values[ind + 2]):
        counter += 1
print(counter)