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

def create_balanced_tree(nodes:TreeNode):
    if not nodes:
        return None
    mid = len(nodes) // 2
    root = TreeNode(nodes[mid])
    root.left = create_balanced_tree(nodes[:mid])
    root.right = create_balanced_tree(nodes[mid+1:])
    return root

def inorder_traversal(root, result):
    if root:
        inorder_traversal(root.left, result)
        result.append(root.val)
        inorder_traversal(root.right, result)

def list_to_tree(input_list, root_node=None, balance=False):
    if not input_list:
        raise ValueError("The input list cannot be empty.")

    # Step 1: Balance the tree if balance=True
    if balance:
        input_list = sorted(input_list)  # Sorting for balanced tree
        root = create_balanced_tree(input_list)
    else:
        # Step 2: Create a binary search tree from the list with a mandatory root_node
        if root_node is None:
            raise ValueError("root_node is required if balance=False.")
        root = TreeNode(root_node)
        for item in input_list:
            if item != root_node:
                root = insert_node(root, item)

    return root



input_list = [30, 20, 40, 10, 35, 50, 5]
list_to_tree(input_list, root_node=25, balance=False)
a = list_to_tree(input_list, balance=True)
a.print()
