# Расстояние Левенштейна не больше 1
def is_similar(text_1, text_2):
    if abs(len(text_1) - len(text_2)) > 1:
        return False
    ind_1 = 0
    ind_2 = 0
    error = False
    if len(text_1) < len(text_2):
        text_1, text_2 = text_2, text_1
    if len(text_1) != len(text_2):
        while ind_1 < len(text_1) and ind_2 < len(text_2):
            if text_1[ind_1] != text_2[ind_2]:
                if error:
                    return False
                error = True
                ind_2 -= 1
            ind_1 += 1
            ind_2 += 1
        return True

    while ind_1 < len(text_1) and ind_2 < len(text_2):
        if text_1[ind_1] != text_2[ind_2]:
            if error:
                return False
            error = True
        ind_1 += 1
        ind_2 += 1
    return True


print(is_similar("abc", "aa"))
