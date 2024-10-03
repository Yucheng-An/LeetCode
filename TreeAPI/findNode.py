from TreeAPI.TreeNode import TreeNode
def findNode(root: TreeNode, value: str | int) -> TreeNode | None:
    """
    Finds a node with the specified value in the tree.
    Args:
        root (TreeNode): The root node of the tree.
        value (str | int): The value to search for.
    Returns:
        TreeNode: The node with the specified value, or None if not found.
    """
    if root is None:
        return None
    if root.val == value:
        return root
    elif value < root.val:
        return findNode(root.left, value)
    else:
        return findNode(root.right, value)
