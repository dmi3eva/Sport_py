n = int(input().strip())
count_positive = 0
line = input().strip()
values = line.split()
for _v in values:
    if int(_v) > 0:
        count_positive += 1
print(count_positive)