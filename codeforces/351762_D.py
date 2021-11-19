line = input()

size = len(line)

pref_a = [0]
pref_b = [0]

for letter in line:
    pref_a.append(pref_a[-1])
    pref_b.append(pref_b[-1])
    if letter == 'a':
        pref_a[-1] += 1
    else:
        pref_b[-1] += 1

answer = 0
for i in range(size + 1):
    for j in range(i, size + 1):
        a_amount = pref_a[i] + (pref_a[-1] - pref_a[j])
        b_amount = pref_b[j] - pref_b[i]
        total = a_amount + b_amount
        answer = max(total, answer)
        if answer == size:
            break
print(answer)
