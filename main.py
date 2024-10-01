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

# Helper function to print tree
def print_tree(root, level=0, label="Root:"):
    if root is not None:
        print(" " * (level * 4) + label + str(root.val))
        print_tree(root.left, level + 1, "L---")
        print_tree(root.right, level + 1, "R---")

def list_to_tree(input_list, root_node=None, balance=False):
    if not input_list:
        return None

    # Step 1: Create a binary search tree from the list
    input_list = sorted(input_list)  # Sorting for balanced tree option
    root_value = root_node if root_node is not None else input_list[0]
    root = TreeNode(root_value)

    for item in input_list:
        if item != root_value:
            root = insert_node(root, item)

    # Step 2: If balance is True, balance the tree
    if balance:
        in_order_nodes = []
        inorder_traversal(root, in_order_nodes)
        root = create_balanced_tree(in_order_nodes)

    # Step 3: Print the tree in the console
    print_tree(root)
    return root


input_list = [30, 20, 40, 10, 35, 50, 5]
list_to_tree(input_list, root_node=25, balance=True)
