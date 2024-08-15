# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def calculateHeight(self, root):
        if not root:
            return 0

        leftHeight = 1 + self.calculateHeight(root.left)
        rightHeight = 1+ self.calculateHeight(root.right)

        return leftHeight if leftHeight > rightHeight else rightHeight

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        leftHeight = self.calculateHeight(root.left)
        rightHeight = self.calculateHeight(root.right)

        if abs(leftHeight - rightHeight) > 1:
            return False
        
        if self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        
        return False

        
        print(leftHeight)
        print(rightHeight)

        

       
        
