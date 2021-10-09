def extract_min_pangram(text: str, alphabet: str) -> str:
    letter_counter = {_w: 0 for _w in alphabet}
    unique_counter = 0
    for i, _letter in enumerate(text):
        letter_counter[_letter] += 1
        if letter_counter[_letter] == 1:
            unique_counter += 1
        if unique_counter == len(alphabet):
            break
    if unique_counter != len(alphabet):
        return None

    best_start = 0
    best_finish = i

    l = 0
    r = i
    while l < r:
        current_symbol = text[l]
        letter_counter[current_symbol] -= 1
        if letter_counter[current_symbol]:
            best_start = l
        else:
            while r < len(text) and text[r] != current_symbol:
                letter_counter[text[r]] += 1
                r += 1

            if r < len(text) and text[r] != current_symbol:
                return text[best_start:best_finish + 1]
            elif (r - l - 1 < best_finish - best_start):
                best_finish = r
                best_start = l + 1
                print(f'Best start now = {best_start}, best finish =  {best_finish}')
        l += 1

    return best_start, best_finish, text[best_start:best_finish + 1]

answer_1 = extract_min_pangram("abcaaab", "abc")
print(answer_1)