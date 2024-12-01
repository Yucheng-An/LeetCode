import TreeHelper
from TreeHelper.TreeNode import TreeNode


def insertNode(root: TreeNode, value: (str | int)) -> TreeNode:
    """
    Inserts a node with the given value into the binary search tree
    If the tree is empty, the value becomes the root

    Args:
        root : TreeNode: input list convert to tree
        value (str | number): The value want to insert
    Returns:
        TreeNode[TreeNode]: inputArray TreeNode after insert
    """
    if root is None:
        return TreeNode(value)
    if value < root.val:
        root.left = insertNode(root.left, value)
    else:
        root.right = insertNode(root.right, value)
    return root


def deleteNode(root: TreeNode, value: (str | int)) -> TreeNode | None:
    """
    Deletes a node with the given value from the binary search tree.
    If the value is not found, it returns the original tree.

    Args:
        root : TreeNode: input TreeNode
        value (str | number): The value want to insert
    Returns:
        TreeNode[TreeNode]: inputArray TreeNode after delete
    """
    if root is None:
        return root
    if value < root.val:
        root.left = deleteNode(root.left, value)
    elif value > root.val:
        root.right = deleteNode(root.right, value)
    else:
        if root.left is None and root.right is None:
            return None
        elif root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            minLargerNode = getMinValueNode(root.right)
            root.value = minLargerNode.val
            root.right = deleteNode(root.right, minLargerNode.val)
    return root


def mergeTrees(tree1: TreeNode | None, tree2: TreeNode | None) -> TreeNode:
    """
    Merges two binary trees into one. If two nodes overlap, their values are summed.
    If a node exists in only one tree, it is directly added to the merged tree.
    Args:
        tree1 : TreeNode: input first tree want to merge
        tree2 : TreeNode: input second tree want to merge
    Returns:
        mergedTree[TreeNode]: inputArray TreeNode after merge
    """
    list1 = TreeHelper.tree2List(tree1)
    list2 = TreeHelper.tree2List(tree2)
    set1 = set(list1)
    set2 = set(list2)
    mergeList = list(set1.symmetric_difference(set2))
    res = TreeHelper.list2Tree(mergeList, balance=True)
    return res


# deleteNode HELPER function, NOT API function
def getMinValueNode(node: TreeNode) -> TreeNode:
    """
    Returns the node with the minimum value in the tree (used for finding the inorder successor then to delete).
    """
    current = node
    while current.left is not None:
        current = current.left
    return current
