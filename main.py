class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

    def printTree(self, level=0, prefix="Root: "):
        if self is not None:
            print(" " * (level * 4) + prefix + str(self.val))
            if self.left:
                self.left.print(level + 1, "L--- ")
            if self.right:
                self.right.print(level + 1, "R--- ")

def list2Tree(inputList: list, root=None, balance=False) -> TreeNode:
    if not inputList:
        raise ValueError("The input list cannot be empty.")
    if balance:
        inputList = sorted(inputList)
        root = createBalancedTree(inputList)
    else:
        if root is None:
            raise ValueError("Root is required if balance=False.")
        root = TreeNode(root)
        for item in inputList:
            if item != root:
                root = insertNode(root, item)
    return root

def insertNode(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.val:
        root.left = insertNode(root.left, value)
    else:
        root.right = insertNode(root.right, value)
    return root

def createBalancedTree(nodes: TreeNode) -> TreeNode:
    if not nodes:
        return None
    mid = len(nodes) // 2
    root = TreeNode(nodes[mid])
    root.left = createBalancedTree(nodes[:mid])
    root.right = createBalancedTree(nodes[mid + 1:])
    return root

def inorderTraversal(root, result):
    if root:
        inorderTraversal(root.left, result)
        result.append(root.val)
        inorderTraversal(root.right, result)




input_list = [30, 20, 40, 10, 35, 50, 5]

balanceTree = list2Tree(input_list, root=25, balance=False)
unbalanceTree = list2Tree(input_list, balance=True)
balanceTree.printTree()
unbalanceTree.printTree()
