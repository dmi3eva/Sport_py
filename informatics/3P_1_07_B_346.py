n = int(input().strip())
count_zeros = 0
count_positive = 0
count_negative = 0
for i in range(n):
    number = int(input())
    if number == 0:
        count_zeros += 1
    if number > 0:
        count_positive += 1
    if number < 0:
        count_negative += 1
answer = f"{count_zeros} {count_positive} {count_negative}"
print(answer)