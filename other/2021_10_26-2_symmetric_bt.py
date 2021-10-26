class BinaryTree:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def is_equal(left: BinaryTree, right: BinaryTree) -> bool:
    if bool(left) ^ bool(right):
        return False
    if not left and not right:
        return True
    if left.value != right.value:
        return False
    return is_equal(left.left, right.right) and is_equal(left.right, right.left)


def is_symmetric(bt: BinaryTree) -> bool:
    return is_equal(bt.left, bt.right)


bt_1 = BinaryTree(5)
bt_2 = BinaryTree(6)
bt_3 = BinaryTree(6)
bt_4 = BinaryTree(7)
bt_5 = BinaryTree(7)
bt_2.left = bt_4
bt_3.right = bt_5
bt_1.left = bt_2
bt_1.right = bt_3
print(is_symmetric(bt_1))
