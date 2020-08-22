# Python program to demonstrate insert operation in binary search tree 
# A utility class that represents an individual node in a BST 


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    # A utility function to insert a new node with the given key 


def insert(root, node):
    if root is None:
        return
    
    if root.val < node.val:
        if root.right is None:
            root.right = node
        else:
            insert(root.right, node)
    
    if root.val > node.val:
        if root.left is None:
            root.left = node
        else:
            insert(root.left, node)
            # A utility function to do inorder tree traversal 
            
            
def search(root, key):
    if root is not None:
        if key > root.val:
            if root.right is not None:
                search(root.right, key)
            else:
                print("not found")
        
        if key < root.val:
            if root.left is not None:
                search(root.left, key)
            else:
                print("not found, smaller")
        
        if key == root.val:
            print("found", key)


def delete(root, key, parent = None):
    currNode = root
    while currNode is not None:
        if key > currNode.val:
            parent = currNode
            currNode = currNode.right
        elif key < currNode.val:
            parent = currNode
            currNode = currNode.left
        else:
            # deleting a node which has two children nodes

            if currNode.left is not None and currNode.right is not None:
                currNode.val = find_min(currNode.right)
                # after replacing the values, now delete that duplicate
                delete(currNode.right, currNode.val, currNode)

            # if the node to be deleted is the root node
            # from here on every node that is to be deleted will have either one child or no child

            elif parent is None:
                # if that one child is the left child
                if currNode.left is not None:
                    currNode.val = find_max(currNode.left)
                    delete(currNode.left, currNode.val, currNode)
                    # currNode.val = currNode.left.val
                    # currNode.right = currNode.left.right
                    # currNode.left = currNode.left.left

                # if that one child is the right child
                if currNode.right is not None:
                    currNode.val = currNode.right.val
                    currNode.left = currNode.right.left
                    currNode.right = currNode.right.right

                else:
                    currNode.val = None

            elif parent.left == currNode:
                parent.left = currNode.left if currNode.left is not None else currNode.right
            elif parent.right == currNode:
                parent.right = currNode.right if currNode.right is not None else  currNode.left

            break
    return root


def inOrder(root):
        if root is not None:
            stack = []
            curr = root
            while True:
                if curr is not None:
                    stack.append(curr)
                    curr = curr.left

                elif stack:
                    node = stack.pop()
                    print(node.val)
                    curr = node.right
                else:
                    break

# this is used to find inorder successor of a node
def find_min(root):
    while root.left:
        root = root.left

    return root.val


def find_max(root):
    while root.right:
        root = root.right

    return root.val

# def inorder(root):
#     inO = []
#     if root:
#         inorder(root.left)
#         print(root.val)
#         inO.append(root.val)
#         inorder(root.right)
#
#     return inO
    # Driver program to test the above functions 


# Let us create the following BST 
#  50
# /	 \ 
# 30	 70 
# / \ / \ 
# 20 40 60 80 
r = Node(50)
insert(r, Node(30))
insert(r, Node(20))
insert(r, Node(40))
insert(r, Node(70))
insert(r, Node(60))
insert(r, Node(80))

# Print inoder traversal of the BST 


delete(r, 30)
delete(r, 50)
inOrder(r)