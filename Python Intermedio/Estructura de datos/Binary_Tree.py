class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return
        current = self.root
        while True:
            if data < current.data:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

    def print_tree(self):
        self._print_node(self.root, "")

    def _print_node(self, node, prefix):
        if node is None:
            return
        self._print_node(node.right, prefix + "    ")
        print(prefix + str(node.data))
        self._print_node(node.left, prefix + "    ")

    def print_inorder(self):
        self._inorder(self.root)

    def _inorder(self, node):
        if node is None:
            return
        self._inorder(node.left)
        print(node.data)
        self._inorder(node.right)


t = BinaryTree()
t.insert(8)
t.insert(3)
t.insert(10)
t.insert(1)
t.insert(6)
t.insert(14)

print("Structure:")
t.print_tree()

print("Data in order :")
t.print_inorder()