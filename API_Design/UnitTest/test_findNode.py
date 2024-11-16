# This will test finding the node of the tree function
from TreeHelper.TreeNode import TreeNode
from TreeHelper.findNode import findNode

def test_emptyTree():
    assert findNode(None, 7) == None

def test_singleNode():
    root = TreeNode(7)
    assert findNode(root, 7) == root

def test_rightNode():
    root = TreeNode(7)
    root.left = TreeNode(5)
    root.right = TreeNode(9)
    assert findNode(root, 9) == root.right

def test_leftNode():
    root = TreeNode(7)
    root.left = TreeNode(5)
    root.right = TreeNode(9)
    assert findNode(root, 5) == root.left

def test_noneNodes():
    root = TreeNode(7)
    root.left = TreeNode(5)
    root.right = TreeNode(9)
    assert findNode(root, 3) == None