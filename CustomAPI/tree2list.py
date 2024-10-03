from CustomAPI.TreeNode import TreeNode

def tree_to_list(root: TreeNode, traversal_type: str = 'inorder') -> list[str | int]:
    """
    Converts a tree to a list based on the specified traversal type.
    Args:
        root (TreeNode): The root node of the tree.
        traversal_type (str, optional): The type of traversal ('inorder', 'preorder', 'postorder').
                                        Default is 'inorder'.
    Returns:
        list[str | int]: A list of values from the tree based on the chosen traversal.

    Raises:
        ValueError: If an invalid traversal type is provided.
    """
    result = []
    if traversal_type == 'inorder':
        inorderTraversal(root, result)
    elif traversal_type == 'preorder':
        preorderTraversal(root, result)
    elif traversal_type == 'postorder':
        postorderTraversal(root, result)
    else:
        raise ValueError("Invalid traversal type. Use 'inorder', 'preorder', or 'postorder'.")
    return result

def inorderTraversal(root: TreeNode, result: list[str | int]):
    if root:
        inorderTraversal(root.left, result)
        result.append(root.val)
        inorderTraversal(root.right, result)

def preorderTraversal(root: TreeNode, result: list[str | int]):
    if root:
        result.append(root.val)
        preorderTraversal(root.left, result)
        preorderTraversal(root.right, result)

def postorderTraversal(root: TreeNode, result: list[str | int]):
    if root:
        postorderTraversal(root.left, result)
        postorderTraversal(root.right, result)
        result.append(root.val)

#
