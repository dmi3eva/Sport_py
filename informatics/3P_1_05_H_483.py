values = input().strip().split()
n, m = int(values[0]), int(values[1])
voices = [0 for _ in range(n)]
amount = 0
for _ in range(m):
    voter_line = input()
    votes_counter = 0
    consignment = -1
    for i, _vote in enumerate(voter_line):
        if _vote == '+':
            votes_counter += 1
            consignment = i
            if votes_counter > 1:
                break
    if votes_counter == 1:
        voices[consignment] += 1
        amount += 1


answer = ""
for i in range(n):
    if voices[i] and voices[i] * 100 >= 7 * amount:
        answer += " " + str(i + 1)

answer = answer.strip()
print(answer)