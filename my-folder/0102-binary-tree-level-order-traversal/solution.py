# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def level(self, curr, result, current_index):
        if not curr:
            return
        
        if current_index >= len(result):
            result.append([curr.val])
        else:
            result[current_index].append(curr.val)

        self.level(curr.left, result, current_index + 1)
        self.level(curr.right, result, current_index + 1)

        return result
        

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        if not root:
            return []

        return self.level(root, result, 0)

        

        
