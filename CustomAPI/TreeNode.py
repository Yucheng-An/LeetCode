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
