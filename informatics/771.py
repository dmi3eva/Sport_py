def are_matching(open_bracket, close_braket):
    matchings = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    return matchings[open_bracket] == close_braket

def solve(sequence):
    stack = []
    for bracket in sequence:
        if bracket in {'(', '[', '{'}:
            stack.append(bracket)
        else:
            if len(stack) == 0:
                return 'no'
            top = stack.pop()
            if not are_matching(top, bracket):
                return 'no'
    if len(stack) > 0:
        return 'no'
    return 'yes'

data = input()
answer = solve(data)
print(answer)