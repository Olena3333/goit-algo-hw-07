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
    else:
        return root

    return root


def min_value_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


if __name__ == "__main__":
    root = None
    keys = [10, 20, 30, 25, 28, 27, -1]

    for key in keys:
        root = insert(root, key)

    min_node = min_value_node(root)
    print("Найменше значення:", min_node.key)


