def find_node(root: TreeNode, value: str | int) -> TreeNode:
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
        return find_node(root.left, value)
    else:
        return find_node(root.right, value)
