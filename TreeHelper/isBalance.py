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
        leftHeight = checkHeight(node.left)
        rightHeight = checkHeight(node.right)
        if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
            return -1
        return max(leftHeight, rightHeight) + 1

    return checkHeight(root) != -1
