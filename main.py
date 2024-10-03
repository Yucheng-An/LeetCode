import TreeAPI

input_list = [30, 20, 40, 10, 35, 50, 5]
input_list2 = ['d', 'b', 'f', 'a', 'e', 'g', 'c']

balanceTree1 = TreeAPI.list2Tree(input_list, root=10, balance=False)
unbalanceTree1 = TreeAPI.list2Tree(input_list, balance=True)

balanceTree2 = TreeAPI.list2Tree(input_list2, root='c', balance=False)
unbalanceTree2 = TreeAPI.list2Tree(input_list2, balance=True)

balanceTree1.printTree()
# unbalanceTree1.printTree()
#
# balanceTree2.printTree()
# unbalanceTree2.printTree()
list1 = TreeAPI.tree2List(balanceTree1, "preorder")
print(TreeAPI.findNode(balanceTree1,30))
