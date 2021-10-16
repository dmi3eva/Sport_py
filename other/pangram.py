def extract_min_pangram(text: str, alphabet: str) -> str:
    letter_counter = {_w: 0 for _w in alphabet}
    unique_counter = 0
    for i, _letter in enumerate(text):
        letter_counter[_letter] = letter_counter.get(_letter, 0) + 1
        if letter_counter[_letter] == 1 and _letter in alphabet:
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
        if letter_counter[current_symbol] or current_symbol not in alphabet:
            if r - l - 1 < best_finish - best_start:
                best_start = l + 1
                best_finish = r
        elif current_symbol in alphabet:
            while r < len(text) - 1 and text[r] != current_symbol:
                r += 1
                letter_counter[text[r]] = letter_counter.get(text[r]) + 1
            if r < len(text) and text[r] != current_symbol:
                return text[best_start:best_finish + 1]
            elif (r - l - 1 < best_finish - best_start):
                letter_counter[current_symbol] += 1
                best_finish = r
                best_start = l + 1
        l += 1

    return text[best_start:best_finish + 1]


answer_1 = extract_min_pangram("abc", "abcd")
print(answer_1)