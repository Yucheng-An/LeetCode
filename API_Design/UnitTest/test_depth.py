# This will test depth of the tree function
from TreeHelper.TreeNode import TreeNode
from TreeHelper.depthOfTree import depthOfTree




def test_should_empty_tree():
    assert depthOfTree(None) == 0

def test_should_empty_tree():
    root = TreeNode(5)
    assert depthOfTree(root) == 1

def test_should_empty_tree():
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    assert depthOfTree(root) == 2