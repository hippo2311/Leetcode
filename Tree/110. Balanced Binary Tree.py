# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        bal = [True]
        def helper(root):
            if not root:
                return 0
            left = helper(root.left)
            if bal[0] is False:
                return 0
            right = helper(root.right)
            if abs(left - right) > 1:
                bal[0] = False
                return 0
            return 1 + max(left, right)
        helper(root)
        return bal[0]
# Time Complexity: O(n)
# Space Complexity: O(h)


        
         