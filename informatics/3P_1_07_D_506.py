line = input().strip()
values = line.split()
k = int(values[0])
n = int(values[1])
page = (n - 1) // k + 1
line = n % k
if line == 0:
    line = k
answer = f"{page} {line}"
print(answer)
