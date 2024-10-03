def depth_of_tree(root: TreeNode) -> int:
    """
    Calculates the depth (height) of the binary tree.

    Args:
        root (TreeNode): The root node of the tree.

    Returns:
        int: The depth of the tree. Returns 0 if the tree is empty.
    """
    if root is None:
        return 0
    left_depth = depth_of_tree(root.left)
    right_depth = depth_of_tree(root.right)
    return max(left_depth, right_depth) + 1
