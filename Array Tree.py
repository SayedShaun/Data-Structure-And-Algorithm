class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_children(self, value):
        self.data(value)

    def print_tree(self, level=0):
        print("   " * level, self.data)
        for child in self.children:
            child.print_tree(level + 1)


root = TreeNode("Electronics")

mobile_node = TreeNode("Mobile")
laptop_node = TreeNode("Laptop")

root.add_children(mobile_node)
root.add_children(laptop_node)

samsung = TreeNode("Samsung")
apple = TreeNode("Apple")

mobile_node.add_children(samsung)
mobile_node.add_children(apple)

dell = TreeNode("Dell")
lenovo = TreeNode("Lenovo")

laptop_node.add_children(dell)
laptop_node.add_children(lenovo)

galaxy_s = TreeNode("Galaxy S Series")
galaxy_note = TreeNode("Galaxy Note Series")

samsung.add_children(galaxy_s)
samsung.add_children(galaxy_note)

root.print_tree()
