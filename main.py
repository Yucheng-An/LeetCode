import CustomAPI

input_list = [30, 20, 40, 10, 35, 50, 5]
input_list2 = ['a','b','c','d','e','f']

balanceTree1 = CustomAPI.list2Tree(input_list, root=25, balance=False)
unbalanceTree1 = CustomAPI.list2Tree(input_list, balance=True)

balanceTree2 = CustomAPI.list2Tree(input_list, root=25, balance=False)
unbalanceTree2 = CustomAPI.list2Tree(input_list, balance=True)

balanceTree1.printTree()
unbalanceTree1.printTree()
