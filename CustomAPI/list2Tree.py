class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

    def printTree(self, level=0, prefix="Root: "):
        if self is not None:
            print(" " * (level * 4) + prefix + str(self.val))
            if self.left:
                self.left.printTree(level + 1, "L--- ")
            if self.right:
                self.right.printTree(level + 1, "R--- ")

def list2Tree(inputList: list[str | int], root: str | int = None, balance: bool = False) -> TreeNode:
    if not inputList:
        raise ValueError("The input list cannot be empty.")

    if balance:
        # Sorting is safe because characters and numbers are consistently compared in Python.
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
