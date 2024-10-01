class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.val = value

def insert_node(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.val:
        root.left = insert_node(root.left, value)
    else:
        root.right = insert_node(root.right, value)
    return root

def create_balanced_tree(nodes):
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

# Helper function to print tree as a real tree
def print_real_tree(root, level=0, prefix="Root: "):
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.val))
        if root.left:
            print_real_tree(root.left, level + 1, "L--- ")
        if root.right:
            print_real_tree(root.right, level + 1, "R--- ")

def list_to_tree(list, root_node=None, balance=False):
    if not list:
        raise ValueError("The input list cannot be empty.")

    # Step 1: Balance the tree if balance=True
    if balance:
        sortedList = sorted(list)  # Sorting for balanced tree
        root = create_balanced_tree(sortedList)
    else:
        # Step 2: Create a binary search tree from the list with a mandatory root_node
        if root_node is None:
            raise ValueError("root_node is required if balance=False.")
        root = TreeNode(root_node)
        for item in list:
            if item != root_node:
                root = insert_node(root, item)

    # Step 3: Print the tree as a real tree in the console
    print_real_tree(root)
    return root


input_list = [30, 20, 40, 10, 35, 50, 5]
list_to_tree(input_list, root_node=25, balance=False)
