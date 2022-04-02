n = int(input())
arc = input()
ghosts = []
hunters = []
ghost_index = 0
hunter_index = 0

for place in arc:
    if place.isupper():
        current_hunter = (place.lower(), hunter_index)
        hunters.append(current_hunter)
        hunter_index += 1
    else:
        current_ghost = (place, ghost_index)

