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


def max_value_node(node):
    current = node
    while current.right is not None:
        current = current.right
    return current


if __name__ == "__main__":
    root = None
    keys = [10, 20, 30, 25, 28, 27, -1]

    for key in keys:
        root = insert(root, key)

    max_node = max_value_node(root)

    print("Найбільше значення:", max_node.key)



