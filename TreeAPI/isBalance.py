from TreeAPI.TreeNode import TreeNode

def is_balanced(root: TreeNode) -> bool:
    """
    Determines if the binary tree is balanced.
    Args:
        root (TreeNode): The root node of the tree.
    Returns:
        bool: True if the tree is balanced, False otherwise.
    """
    def check_height(node):
        if node is None:
            return 0
        left_height = check_height(node.left)
        right_height = check_height(node.right)
        if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height) + 1

    return check_height(root) != -1
