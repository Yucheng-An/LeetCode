from TreeHelper.TreeNode import TreeNode

def isBalanced(root: TreeNode) -> bool:
    """
    Determines if the binary tree is balanced.
    Args:
        root (TreeNode): The root node of the tree.
    Returns:
        bool: True if the tree is balanced, False otherwise.
    """
    def checkHeight(node):
        if node is None:
            return 0
        left_height = checkHeight(node.left)
        right_height = checkHeight(node.right)
        if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height) + 1

    return checkHeight(root) != -1
