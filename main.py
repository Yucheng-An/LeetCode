import CustomAPI

input_list = [30, 20, 40, 10, 35, 50, 5]
input_list2 = ['a','b','c','d','e','f']

balanceTree = CustomAPI.list2Tree(input_list, root=25, balance=False)
unbalanceTree = CustomAPI.list2Tree(input_list, balance=True)

balanceTree = CustomAPI.list2Tree(input_list, root=25, balance=False)
unbalanceTree = CustomAPI.list2Tree(input_list, balance=True)

balanceTree.printTree()
unbalanceTree.printTree()
