
def in_one_case(symbol_1, symbol_2):
    upper = symbol_1.isupper() and symbol_2.isupper()
    lower = symbol_1.islower() and symbol_2.islower()
    return upper or lower

n = int(input())
arc = input()
stack = []
hunters = {}  # Положение охотника на окружности: его порядковый номер
ghosts = {}  # Положение привидения на окружности: его порядковый номер
answers = [None] * n



for ind, place in enumerate(arc):
    if place.isupper():  # Если встретили охотника, сохраняем его позицию
        hunters[ind] = len(hunters) + 1
    else:  # Если встретили привидение, сохраняем его позицию
        ghosts[ind] = len(ghosts) + 1

    if len(stack) == 0:
        stack.append(ind)
    elif arc[stack[-1]].lower() != place.lower():  # Типы не совпадают
        stack.append(ind)
    elif in_one_case(arc[stack[-1]], place):  # Оба охотники или оба привидения
        stack.append(ind)
    else:  # Выстрел возможен
        from_stack = stack.pop()
        if arc[from_stack].isupper():  # Выясняем, кто тут охотник
            hunter_number = hunters[from_stack]
            ghost_number = ghosts[ind]
        else:
            hunter_number = hunters[ind]
            ghost_number = ghosts[from_stack]
        answers[hunter_number] = str(ghost_number)
if len(stack) > 0:
    print("Impossible")
else:
    print(" ".join(stack))


"""
Test #1
DabBCcAdaA
-> 4 2 3 1 5
"""







