

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def preorder_traversal(root):

    if root is None:
        return float("NaN")

    min_value = root.val

    min_left = preorder_traversal(root.left)
    min_right = preorder_traversal(root.right)

    return min(min_value, min_left, min_right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)


if __name__ == "__main__":

    def max_value(root):
        result = preorder_traversal(root)
        print(result)

    max_value(root)
