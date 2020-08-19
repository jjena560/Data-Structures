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

    ## recursive methods

    # def inorder(self, node):
    #     if node is not None:
    #         self.inorder(node.left)
    #         print(node.value)
    #         self.inorder(node.right)
    #
    # def preorder(self, node):
    #     if node is not None:
    #         print(node.value)
    #         self.preorder(node.left)
    #         self.preorder(node.right)

    # iterative methods

    def preorder(self, root):
        if root is None:
            return
        stack = [root]

        while len(stack) > 0:
            node = stack.pop()
            print(node.value)

            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)


    def inorder(self, root):

        if root is None:
            return

        stack = []
        curr = root


        while True:

            if curr is not None:
                stack.append(curr)
                curr = curr.left

            elif stack:
                node = stack.pop()
                print(node.value)

                curr = node.right

            else:
                break

    def postorder(self, root):
        if root is None:
            return
        
        stack1 = []
        stack2 = []
        
        stack1.append(root)
        
        while len(stack1) > 0:
            node = stack1.pop()
            stack2.append(node)

            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)

        while len(stack2) > 0:
            node = stack2.pop()
            print(node.value)


    
    
tree = BinarySearchTree()
tree.insert(10)
tree.insert(5)
tree.insert(3)
tree.insert(13) 
tree.insert(7)
tree.insert(23)


tree.postorder(tree.root)