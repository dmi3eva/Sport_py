from collections import deque
def init(root, tree):
    pref = [0]
    queue = deque()
    queue.append([root, 0, 0])
    layer_num = 0
    prev_layer = 0
    layer_sum = 0
    while len(queue) > 0:
        current_node = queue.popleft()
        current = current_node[0]
        if current_node[1] > prev_layer:
            pref.append(pref[-1] + layer_sum)
            layer_sum = 0
            prev_layer += 1
        if current not in tree.keys():
            continue
        children = tree[current]
        for child, dist in children.items():
            layer_sum += dist + current_node[2]
            queue.append([child, layer_num + 1, current_node[2] + dist])
    pref.append(pref[-1] + layer_sum)
    return pref


def solve(pref, l: int, r: int) -> int:
    return pref[r] - pref[l]


tree = {
    1: {
        2: 10,
        3: 20
    },
    2: {
        4: 30
    }
}

root = 1
pref_ex = [0, 30, 70]
requests = [(1, 2), (0, 2)]
pref = init(root, tree)
print(pref)
for _r in requests:
    print(solve(pref, _r[0], _r[1]))