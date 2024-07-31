class Tree:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None

def inorder(root):
    if root is None:
        return []
    return inorder(root.left)+[root.value]+inorder(root.right)

def preorder(root):
    if root is None:
        return []
    return [root.value]+preorder(root.left)+preorder(root.right)

def lastorder(root):
    if root is None:
        return []
    return lastorder(root.left)+lastorder(root.right)+[root.value]

def maxlength(root):
    if root is None:
        return 0
    else:
        left_length=maxlength(root.left)
        right_lenth=maxlength(root.right)
        return max(left_length,right_lenth)+1

root=Tree((0,0))
root.right=Tree((1,0))
root.left=Tree((-1,0))
root.left.left=Tree((-1,-1))
root.right.left=Tree((1,1))
root.right.left.left=Tree((2,1))
print(maxlength(root))