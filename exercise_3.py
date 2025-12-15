class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None


def insert(root, key):
    if not root:
        return AVLNode(key)

    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)

    return root


def sum_of_tree(node):
    if node is None:
        return 0
    return node.key + sum_of_tree(node.left) + sum_of_tree(node.right)


if __name__ == "__main__":
    root = None
    keys = [10, 20, 30, 25, 28, 27, -1]

    for key in keys:
        root = insert(root, key)

    total_sum = sum_of_tree(root)
    print("Сума всіх значень у дереві:", total_sum)