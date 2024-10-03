from CustomAPI.list2Tree import TreeNode


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

# Helper functions for tree traversal:
def preorderTraversal(root, result):
    if root:
        result.append(root.val)
        preorderTraversal(root.left, result)
        preorderTraversal(root.right, result)

def postorderTraversal(root, result):
    if root:
        postorderTraversal(root.left, result)
        postorderTraversal(root.right, result)
        result.append(root.val)
