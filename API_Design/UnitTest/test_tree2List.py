# This unit for testing function 'tree2list' in TreeHelper
from TreeHelper.TreeNode import TreeNode
from TreeHelper.tree2List import tree2List
from pytest import raises

def creatTestTree1():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    return root
def creatTestTree2():
    root = TreeNode(9)
    root.left = TreeNode(8)
    root.right = TreeNode(7)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(5)
    return root
def creatTestTree3():
    root = TreeNode(100)
    root.right = TreeNode(110)
    root.right.left = TreeNode(108)
    root.right.right = TreeNode(115)
    root.right.right.left = TreeNode(113)
    root.right.right.right = TreeNode(120)
    root.right.right.right.left = TreeNode(119)
    root.right.right.right.right = TreeNode(130)
    root.right.right.right.right.left = TreeNode(125)
    root.right.right.right.right.right = TreeNode(137)
    return root
def createTestTree4():
    root = TreeNode(50)
    root.right = TreeNode(55)
    root.right.right = TreeNode(60)
    root.right.right.right = TreeNode(65)
    root.right.right.right.right = TreeNode(70)
    root.right.right.right.right.right = TreeNode(75)
    root.right.right.right.right.right.right = TreeNode(80)
    root.right.right.right.right.right.right.right = TreeNode(85)
    return root
def creatInvalidTree1():
    root = TreeNode(9)
    root.left = TreeNode(8)
    root.right = TreeNode('a')
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(5)
    return root


def test_traversal_tree1_should_inorder():
    root = creatTestTree1()
    expectedResult = [4, 2, 5, 1, 3]
    assert tree2List(root, 'inorder') == expectedResult


def test_traversal_tree1_should_preorder():
    root = creatTestTree1()
    expectedResult = [1, 2, 4, 5, 3]
    assert tree2List(root, 'preorder') == expectedResult


def test_traversal_tree1_should_postorder():
    root = creatTestTree1()
    expectedResult = [4, 5, 2, 3, 1]
    assert tree2List(root, 'postorder') == expectedResult


def test_traversal_tree2_should_inorder():
    root = creatTestTree2()
    expectedResult = [6, 8, 5, 9, 7]
    assert tree2List(root, 'inorder') == expectedResult


def test_traversal_tree2_should_preorder():
    root = creatTestTree2()
    expectedResult = [9, 8, 6, 5, 7]
    assert tree2List(root, 'preorder') == expectedResult


def test_traversal_tree2_should_postorder():
    root = creatTestTree2()
    expectedResult = [6, 5, 8, 7, 9]
    assert tree2List(root, 'postorder') == expectedResult

def test_traversal_big_tree3_should_inorder():
    root = creatTestTree3()
    expectedResult = [100, 108, 110, 113, 115, 119, 120, 125, 130, 137]
    assert tree2List(root, 'inorder') == expectedResult


def test_traversal_big_tree3_should_preorder():
    root = creatTestTree3()
    expectedResult = [100, 110, 108, 115, 113, 120, 119, 130, 125, 137]
    assert tree2List(root, 'preorder') == expectedResult


def test_traversal_big_tree3_should_postorder():
    root = creatTestTree3()
    expectedResult = [108, 113, 119, 125, 137, 130, 120, 115, 110, 100]
    assert tree2List(root, 'postorder') == expectedResult

def test_traversal_linear_tree_tree4_should_inorder():
    root = createTestTree4()
    expectedResult = [50, 55, 60, 65, 70, 75, 80, 85]
    assert tree2List(root, 'inorder') == expectedResult


def test_traversal_linear_tree_tree4_should_preorder():
    root = createTestTree4()
    expectedResult = [50, 55, 60, 65, 70, 75, 80, 85]
    assert tree2List(root, 'preorder') == expectedResult


def test_traversal_linear_tree_tree4_should_postorder():
    root = createTestTree4()
    expectedResult = [85, 80, 75, 70, 65, 60, 55, 50]
    assert tree2List(root, 'postorder') == expectedResult

# Tree is empty
def test_empty_tree():
    emptyRoot = None
    expectedResult = []
    assert tree2List(emptyRoot, 'inorder') == expectedResult
    assert tree2List(emptyRoot, 'preorder') == expectedResult
    assert tree2List(emptyRoot, 'postorder') == expectedResult

# Tree with ONE node
def test_only_one_single_node_tree():
    root = TreeNode(10)
    expectedResult = [10]
    assert tree2List(root, 'inorder') == expectedResult
    assert tree2List(root, 'preorder') == expectedResult
    assert tree2List(root, 'postorder') == expectedResult

# invalid traversal type 1
def test_empty_traversal_raises_error_message1():
    root = creatTestTree2()
    with raises(ValueError, match="Invalid traversal type. Use 'inorder', 'preorder', or 'postorder'."):
        tree2List(root, None)

# invalid traversal type 2
def test_invalid_traversal_raises_error_message1():
    root = creatInvalidTree1()
    with raises(ValueError):
        tree2List(root, 'invalid_type')
