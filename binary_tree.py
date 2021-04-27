class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, print_type):
        if print_type == 'preorder':
            return self.print_pre_order(self.root, "")
        elif print_type == 'inorder':
            return self.print_inorder(self.root, "")
        elif print_type == 'postorder':
            return self.print_postorder(self.root, "")
        else:
            return f"{print_type} not supported"

    def print_pre_order(self, start, traversal):
        """ Root -> Left -> Right """
        if start:
            traversal += f"{str(start.data)} "
            traversal = self.print_pre_order(start.left, traversal)
            traversal = self.print_pre_order(start.right, traversal)
        return traversal
    
    def print_inorder(self, start, traversal):
        """ Left -> Root -> Right """
        if start:
            traversal = self.print_inorder(start.left, traversal)
            traversal += f"{str(start.data)} "
            traversal = self.print_inorder(start.right, traversal)
        return traversal
    
    def print_postorder(self, start, traversal):
        """ Left -> Root -> Right """
        if start:
            traversal = self.print_postorder(start.left, traversal)
            traversal = self.print_postorder(start.right, traversal)
            traversal += f"{str(start.data)} "
        return traversal


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(5)
tree.root.left.left = Node(612)
tree.root.left.right = Node(21)

print(tree.print_tree('preorder'))
print(tree.print_tree('inorder'))
print(tree.print_tree('postorder'))