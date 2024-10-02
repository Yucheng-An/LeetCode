class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.val = value

    # Method to print the tree
    def print(self, level=0, prefix="Root: "):
        if self is not None:
            print(" " * (level * 4) + prefix + str(self.val))
            if self.left:
                self.left.print(level + 1, "L--- ")
            if self.right:
                self.right.print(level + 1, "R--- ")


def insert_node(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.val:
        root.left = insert_node(root.left, value)
    else:
        root.right = insert_node(root.right, value)
    return root


def create_balanced_tree(nodes: TreeNode) -> TreeNode:
    if not nodes:
        return None
    mid = len(nodes) // 2
    root = TreeNode(nodes[mid])
    root.left = create_balanced_tree(nodes[:mid])
    root.right = create_balanced_tree(nodes[mid + 1:])
    return root


def inorder_traversal(root, result):
    if root:
        inorder_traversal(root.left, result)
        result.append(root.val)
        inorder_traversal(root.right, result)


def list2Tree(inputList: list, root=None, balance=False) -> TreeNode:
    if not inputList:
        raise ValueError("The input list cannot be empty.")
    if balance:
        inputList = sorted(inputList)
        root = create_balanced_tree(inputList)
    else:
        if root is None:
            raise ValueError("Root is required if balance=False.")
        root = TreeNode(root)
        for item in inputList:
            if item != root:
                root = insert_node(root, item)

    return root


input_list = [30, 20, 40, 10, 35, 50, 5]
list_to_tree(input_list, root=25, balance=False)
a = list_to_tree(input_list, balance=True)
a.print()
