# Палиндромы
def solve(text):
    l = 0
    r = len(text) - 1
    while l < r and l < len(text) and r >= 0:
        while l < len(text) and not text[l].isalpha():  # На continue
            l += 1
        while r >= 0 and not text[r].isalpha():
            r -= 1
        if l < r and text[l] != text[r]:
            return False
        l += 1
        r -= 1
    return True


if __name__ == "__main__":
    text = input()
    print(solve(text))
