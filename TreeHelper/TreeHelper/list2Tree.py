from TreeHelper.TreeNode import TreeNode
from TreeHelper.manipulation import insertNode

def list2Tree(inputList: list[str | int], root: str | int = None, balance: bool = False) -> TreeNode:
    """
    Converts a list to a tree based on the specified root or balance.
    Args:
        inputList (str | number): input list convert to tree.
        root (str | number, optional): Assign specified root or not.
                                        Default is 'None'.
        balance (bool, optional): Whether to balance the tree.
                                        Default is False.
    Returns:
        TreeNode[TreeNode]: A TreeNode start from root.
    Raises:
        TypeError : Input list must contain either all strings or all integers.
        ValueError: Root is required if balance=False.
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

def createBalancedTree(nodes: list[str | int]) -> TreeNode | None:
    if not nodes:
        return None
    mid = len(nodes) // 2
    root = TreeNode(nodes[mid])
    root.left = createBalancedTree(nodes[:mid])
    root.right = createBalancedTree(nodes[mid + 1:])
    return root


