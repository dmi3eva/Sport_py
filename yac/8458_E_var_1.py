
def solve(s1, s2):
    amounts_1 = {}
    amounts_2 = {}
    for letter in s1:
        amounts_1[letter] = amounts_1.get(letter, 0) + 1
    for letter in s2:
        amounts_2[letter] = amounts_2.get(letter, 0) + 1
    for _k, _v in amounts_1.items():
        if _k not in amounts_2.keys():
            return '0'
        if _v != amounts_2[_k]:
            return '0'
        del amounts_2[_k]
    if len(amounts_2) > 0:
        return '0'
    else:
        return '1'

s1 = input()
s2 = input()
print(solve(s1, s2))

