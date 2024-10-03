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

# Helper function for inorder traversal:
def inorderTraversal(root: TreeNode, result: list[str | int]):
    if root:
        inorderTraversal(root.left, result)
        result.append(root.val)
        inorderTraversal(root.right, result)

# Helper function for preorder traversal:
def preorderTraversal(root: TreeNode, result: list[str | int]):
    if root:
        result.append(root.val)
        preorderTraversal(root.left, result)
        preorderTraversal(root.right, result)

# Helper function for postorder traversal:
def postorderTraversal(root: TreeNode, result: list[str | int]):
    if root:
        postorderTraversal(root.left, result)
        postorderTraversal(root.right, result)
        result.append(root.val)

# Example usage:
if __name__ == "__main__":
    # Creating a sample tree
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(12)
    root.right.right = TreeNode(20)

    # Convert the tree to a list using inorder traversal
    inorder_list = tree_to_list(root, 'inorder')
    print("Inorder Traversal:", inorder_list)

    # Convert the tree to a list using preorder traversal
    preorder_list = tree_to_list(root, 'preorder')
    print("Preorder Traversal:", preorder_list)

    # Convert the tree to a list using postorder traversal
    postorder_list = tree_to_list(root, 'postorder')
    print("Postorder Traversal:", postorder_list)
