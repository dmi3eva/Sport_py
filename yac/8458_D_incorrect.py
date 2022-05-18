def generate_new_iteration(previous):
    new_iteration = set()
    for rbs in previous:
        if f"({rbs})" not in new_iteration:
            new_iteration.add(f"({rbs})")
        if f"(){rbs}" not in new_iteration:
            new_iteration.add(f"(){rbs}")
        if f"{rbs}()" not in new_iteration:
            new_iteration.add(f"{rbs}()")
    return list(new_iteration)


n = int(input())
previous_iteration = [""]
for _ in range(n):
    new_iteration = generate_new_iteration(previous_iteration)
    previous_iteration = new_iteration
previous_iteration.sort()
print('\n'.join(previous_iteration))
