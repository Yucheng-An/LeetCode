"""
Since Python3 doesn't have build-in Tree structure.
Constructed basic Tree structure, import this class into each function.
Included a class method "printTree" for print out Tree structure in terminal.
"""
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

    def printTree(self, level=0, prefix="Root: "):
        if self.right is not None:
            self.right.printTree(level + 1, "    " * (level + 1) + "R-- ")
        print("    " * level + prefix + str(self.val))
        if self.left is not None:
            self.left.printTree(level + 1, "    " * (level + 1) + "L-- ")
