def verify(sequence):
    output_line = ''.join(sequence)
    print(output_line)


def generate(sequence, k, position):
    if position >= len(sequence) and k == 0:
        verify(sequence)
    elif 0 <= k <= len(sequence) - position:
        sequence[position] = '0'
        generate(sequence, k, position + 1)
        sequence[position] = '1'
        generate(sequence, k - 1, position + 1)


if __name__ == "__main__":
    n, k = [int(x) for x in input().strip().split(' ')]
    sequence = ['0' for _ in range(n)]
    generate(sequence, k, 0)
