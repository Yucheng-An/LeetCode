from TreeAPI.TreeNode import TreeNode

def list2Tree(inputList: list[str | int], root: str | int = None, balance: bool = False) -> TreeNode:
    """
    Converts a list to a tree based on the specified root or balance.
    Args:
        inputList (str | number): The root node of the tree.
        traversal_type (str, optional): The type of traversal ('inorder', 'preorder', 'postorder').
                                        Default is 'inorder'.
    Returns:
        list[str | int]: A list of values from the tree based on the chosen traversal.

    Raises:
        ValueError: If an invalid traversal type is provided.
    """

    if not inputList:
        raise ValueError("The input list cannot be empty.")
    first_type = type(inputList[0])
    if not all(isinstance(item, first_type) for item in inputList):
        raise TypeError("Input list must contain either all strings or all integers.")
    if balance:
        inputList = sorted(inputList)
        root = createBalancedTree(inputList)
    else:
        if root is None:
            raise ValueError("Root is required if balance=False.")
        root = TreeNode(root)
        for item in inputList:
            if item != root.val:
                root = insertNode(root, item)
    return root

def insertNode(root: TreeNode, value: str | int) -> TreeNode:
    if root is None:
        return TreeNode(value)
    if value < root.val:
        root.left = insertNode(root.left, value)
    else:
        root.right = insertNode(root.right, value)
    return root

def createBalancedTree(nodes: list[str | int]) -> TreeNode:
    if not nodes:
        return None
    mid = len(nodes) // 2
    root = TreeNode(nodes[mid])
    root.left = createBalancedTree(nodes[:mid])
    root.right = createBalancedTree(nodes[mid + 1:])
    return root

def inorderTraversal(root: TreeNode, result: list[str | int]):
    if root:
        inorderTraversal(root.left, result)
        result.append(root.val)
        inorderTraversal(root.right, result)


