import list2Tree from CustomAPI

input_list = [30, 20, 40, 10, 35, 50, 5]

balanceTree = list2Tree(input_list, root=25, balance=False)
unbalanceTree = list2Tree(input_list, balance=True)
balanceTree.printTree()
unbalanceTree.printTree()
