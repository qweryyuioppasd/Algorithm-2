# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        return self.postorderTraversal(root.left)+self.postorderTraversal(root.right)+[root.val]
    
root=TreeNode(1)
root.left=TreeNode(0)
root.right=TreeNode(2)
root.left.left=TreeNode(3)
s1=Solution()
print(s1.postorderTraversal(root))