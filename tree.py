class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorder_traversal(node):

    print(node.value, end=" ")
    if node.left != None:
        inorder_traversal(node.left)
    if node.right !=None:
        inorder_traversal(node.right)

# Create a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Perform an inorder traversal
print("Inorder traversal:", end=" ")
inorder_traversal(root)
