# constructing a tree from given traversals

class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def buildTree(inOrder, preOrder, start, end):
    if start > end:
        return

    tNode = TreeNode(preOrder[buildTree.preIndex])
    buildTree.preIndex += 1

    if start == end:
        return tNode

    # find the index of this node in inOrder traversal array
    inIndex = search(inOrder, tNode.value)

    # constructing left and right subtree
    tNode.left = buildTree(inOrder, preOrder, start, inIndex - 1)
    tNode.right = buildTree(inOrder, preOrder, inIndex + 1, end)

    return tNode




def search(arr, value):
    for i in range(len(arr)-1):
        if arr[i] == value:
            return i


def InOrder(root):
    if root is None:
        return

    stack = []
    curr = root

    while True:
        while curr:
            stack.append(curr)
            curr = curr.left

        if stack:
            node = stack.pop()
            print(node.value)
            curr = node.right

        else:
            break




buildTree.preIndex = 0

preOrder = [4, 7, 9, 6, 3, 2, 5, 8, 1]
inOrder = [7, 6, 9, 3, 4, 5, 8, 2, 1]

root = buildTree(inOrder, preOrder, 0, len(inOrder) - 1)

InOrder(root)