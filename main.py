import CustomAPI

input_list = [30, 20, 40, 10, 35, 50, 5]
input_list2 = ['d', 'b', 'f', 'a', 'e', 'g', 'c']

balanceTree1 = CustomAPI.list2Tree(input_list, root=25, balance=False)
unbalanceTree1 = CustomAPI.list2Tree(input_list, balance=True)

balanceTree2 = CustomAPI.list2Tree(input_list2, root='c', balance=False)
unbalanceTree2 = CustomAPI.list2Tree(input_list2, balance=True)

# balanceTree1.printTree()
# unbalanceTree1.printTree()
#
# balanceTree2.printTree()
# unbalanceTree2.printTree()
list1 = 
