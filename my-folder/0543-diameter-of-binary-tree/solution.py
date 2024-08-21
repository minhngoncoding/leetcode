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
        rightHeight = 1 + self.calculateHeight(root.right)

        return leftHeight if leftHeight > rightHeight else rightHeight

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        leftDiameter = self.diameterOfBinaryTree(root.left)
        rightDiameter = self.diameterOfBinaryTree(root.right)

        currentDiameter = self.calculateHeight(root.left) + self.calculateHeight(root.right)

        return max(currentDiameter, leftDiameter, rightDiameter)

        
