n = int(input())
current_seq_size = 0
max_size = 0
for i in range(n):
    bit = int(input())
    if bit == 1:
        current_seq_size += 1
    else:
        if current_seq_size > max_size:
            max_size = current_seq_size
        current_seq_size = 0
if current_seq_size > max_size:
    max_size = current_seq_size
print(max_size)