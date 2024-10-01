from graphviz import Digraph


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, key):
    if root is None:
        return Node(key)

    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)


# Create the root
root = Node(50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

print("Inorder traversal of the binary tree:")
inorder(root)


def visualize_tree(root):
    dot = Digraph()

    def add_edges(node):
        if node:
            if node.left:
                dot.edge(str(node.val), str(node.left.val))
                add_edges(node.left)
            if node.right:
                dot.edge(str(node.val), str(node.right.val))
                add_edges(node.right)

    add_edges(root)
    return dot


# Create and display the tree visualization
tree_visualization = visualize_tree(root)
tree_visualization.render('binary_tree', view=True)
