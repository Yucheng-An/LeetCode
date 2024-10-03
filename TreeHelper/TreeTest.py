# Import API
import TreeHelper

# Make two list for test
iList = [30, 20, 40, 10, 35, 50, 5]
iList2 = ['d', 'b', 'f', 'a', 'e', 'g', 'c']
# unbalanceTree2 = TreeHelper.list2Tree(input_list2, root='c', balance=False)
# balanceTree2 = TreeHelper.list2Tree(input_list2, balance=True)

# Call list2Tree method
print("Start testing list2Tree() method")
unbalanceTree1 = TreeHelper.list2Tree(iList, root=20, balance=False)
balanceTree1 = TreeHelper.list2Tree(iList, balance=True)
print("UnbalanceTree1")
unbalanceTree1.printTree()
print("BalanceTree1")
balanceTree1.printTree()
print("End")
print("======================================================")

# Call tree2List method
print("Start testing tree2List() method")
list1 = TreeHelper.tree2List(balanceTree1, "preorder")
list2 = TreeHelper.tree2List(unbalanceTree1, "inorder")
print(f"Preorder Tree: {list1}")
print(f"Inorder Tree: {list2}")
print("End")
print("======================================================")

# unbalanceTree2 = TreeHelper.list2Tree(input_list2, root='c', balance=False)
# balanceTree2 = TreeHelper.list2Tree(input_list2, balance=True)

# Call depthOfTree method
print("Start testing depthOfTree() method")
print(f"UnbalanceTree1 depth: {TreeHelper.depthOfTree(unbalanceTree1)}")
print(f"BalanceTree1 depth: {TreeHelper.depthOfTree(balanceTree1)}")
print("End")
print("======================================================")

# Call isBalanced method
print("Start testing isBalanced() method")
print(f"UnbalanceTree1 depth: {TreeHelper.isBalanced(unbalanceTree1)}  | Expect: False")
print(f"BalanceTree1 depth: {TreeHelper.isBalanced(balanceTree1)}  | Expect: True")
print("End")
print("======================================================")

# Call findNode method
print("Start testing findNode() method")
TreeHelper.findNode(balanceTree1, 40).printTree()
print("End")
print("======================================================")
