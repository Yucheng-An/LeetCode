import TreeHelper

input_list = [30, 20, 40, 10, 35, 50, 5]
input_list2 = ['d', 'b', 'f', 'a', 'e', 'g', 'c']

unbalanceTree1 = TreeHelper.list2Tree(input_list, root=20, balance=False)
balanceTree1 = TreeHelper.list2Tree(input_list, balance=True)

unbalanceTree2 = TreeHelper.list2Tree(input_list2, root='c', balance=False)
balanceTree2 = TreeHelper.list2Tree(input_list2, balance=True)

balanceTree1.printTree()
# unbalanceTree1.printTree()
#
# balanceTree2.printTree()
# unbalanceTree2.printTree()
list1 = TreeHelper.tree2List(balanceTree1, "preorder")
print("11111111111111111111111111111111111")
TreeHelper.findNode(balanceTree1, 000).printTree()
print(TreeHelper.depthOfTree(balanceTree1))
print(TreeHelper.isBalanced(unbalanceTree1))
print(TreeHelper.isBalanced(balanceTree1))
