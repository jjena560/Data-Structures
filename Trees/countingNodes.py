class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        temp = TreeNode(value)

        if self.root is None:
            self.root = temp
            return
        else:
            curr = self.root
            while True:
                if value == curr.value:
                    return
                if value < curr.value:
                    if curr.left is None:
                        curr.left = temp
                        return
                    curr = curr.left
                elif value > curr.value:
                    if curr.right is None:
                        curr.right = temp
                        return
                    curr = curr.right

    def count(self, root):

        if root is not None:
            # count the nodes in left subtree
            x = self.count(root.left)
            # count the nodes in left subtree
            y = self.count(root.right)
            return x + y + 1
        
        return 0 

    def search(self, key):
        if self.root is None:
            print("NULL tree")
            return
        curr = self.root
        found = False
        while curr and not found:
            if key < curr.value:
                curr = curr.left
            elif key > curr.value:
                curr = curr.right
            else:
                found = True

        if found:
            return curr.value
        else:
            return "Not found"


tree = BinarySearchTree()
tree.insert(10)
tree.insert(5)
tree.insert(3)
tree.insert(13)
tree.insert(7)
tree.insert(23)
tree.insert(44)

print(tree.count(tree.root))