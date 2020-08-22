class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

class BST:
    def constructTree(self, pre, size):

        # creating the first element of pre as the root Node
        root = Node(pre[0])
        
        stack = [root]
        i = 1

        # empty stack
        while i < size:
            temp = None
            
            while len(stack) > 0 and pre[i] > stack[-1].val:
                temp = stack.pop()
            if temp:
                temp.right = Node(pre[i])
                stack.append(temp.right)
            else:
                temp = stack[-1]
                temp.left = Node(pre[i])
                stack.append(temp.left)
            i += 1
        
        return root

    def inOrder(self, root):
        if root is None:
            return

        currNode = root
        stack = []

        while True:

            if currNode is not None:
                stack.append(currNode)
                currNode = currNode.left

            elif stack:
                node = stack.pop()
                print(node.val)
                currNode = node.right

            else:
                break

pre = [10, 5, 1, 7, 40, 50]
size = len(pre)
root = BST()
root.constructTree(pre, size)
root.inOrder(root.constructTree(pre, size))