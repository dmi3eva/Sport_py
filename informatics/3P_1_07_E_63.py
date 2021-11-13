n = int(input().strip())
count_positive = 0
line = input().strip()
values = line.split()
answer = ""
for i, v in enumerate(values):
    if i % 2 == 0:
        answer += f"{v} "
answer = answer.strip()
print(answer)