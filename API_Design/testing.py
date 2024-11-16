import random
import TreeHelper
from TreeHelper.TreeNode import TreeNode

# Notes:
# Ramis: Found a bug. If you run tests several time, it will fail one of the tests. Needs to be investigated
# As a result, test_random_Tree() fails sometimes. Needs to be investigated


# Functions
# Create a random tree. Returns tuple of tree, if balanced or not
def randomTree():
    balanced = random.choice([True, False])
    size = random.randint(3, 10)
    nList = [random.randint(1,50) for _ in range(size)]

    if balanced:
        return (TreeHelper.list2Tree(nList, nList[random.randint(0, size - 1)], False), balanced)
    else:
        return (TreeHelper.list2Tree(nList, None, True), balanced)
    

# Tests
# Test balancing tree
def test_balanced_tree():
    tree = TreeHelper.list2Tree([random.randint(1,50) for _ in range(random.randint(3, 10))], None, True)
    tree.printTree()
    assert TreeHelper.isBalanced(tree) == True

# Test nonbalanced tree
def test_non_balanced_tree():
    tList = [random.randint(1,50) for _ in range(random.randint(3,10))]
    tree = TreeHelper.list2Tree(tList, tList[(random.randint(0, len(tList) - 1))], False)
    tree.printTree()
    assert TreeHelper.isBalanced(tree) == False

# Test generating random tree and checking if it's balanced
def test_random_tree():
    randomTuple = randomTree()
    generatedTree = randomTuple[0]
    randomTreeBalanced = randomTuple[1]
    print(f"Random tree is balanced: {randomTreeBalanced}")

    assert TreeHelper.isBalanced(generatedTree) == randomTreeBalanced
