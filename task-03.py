

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def preorder_traversal(root):
    if root is None:
        return 0

    result = root.val

    left_value = preorder_traversal(root.left)
    right_value = preorder_traversal(root.right)

    return result + left_value + right_value


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)


if __name__ == "__main__":

    def sum_value(root):
        result = preorder_traversal(root)
        print(f"Сума всіх значень у дереві: {result}")

    sum_value(root)
