def calculate_cosine(descr_1, descr_2):
    pointer_1 = 0
    pointer_2 = 0
    cosine = 0
    while pointer_1 < len(descr_1) and pointer_2 < len(descr_2):
        segment_1 = descr_1[pointer_1]
        segment_2 = descr_2[pointer_2]
        if segment_1[0] > segment_2[0]:
            pointer_2 += 1
            descr_1[pointer_1] = (segment_1[0] - segment_2[0], segment_1[1],)
        elif segment_2[0] > segment_1[0]:
            pointer_1 += 1
            descr_2[pointer_2] = (segment_2[0] - segment_1[0], segment_2[1])
        else:
            pointer_1 += 1
            pointer_2 += 1
        addee = min(segment_1[0], segment_2[0]) * segment_1[1] * segment_2[1]
        cosine += addee
    if pointer_1 < len(descr_1) or pointer_2 < len(descr_2):
        return None
    return cosine


descr_1 = [(3, 1), (4, 2), (2, 3)]
descr_2 = [(3, 5), (3, 6), (3, 7)]

# descr_1 = [(5, 1), (1, 1)]
# descr_2 = [(1, 1), (5, 1)]

print(calculate_cosine(descr_1, descr_2))