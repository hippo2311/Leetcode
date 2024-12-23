# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if p == None and q == None:
        #     return True
        # return str(p) == str(q)        
        def check(p,q):
            if not p and not q:
                return True
            if (not p and q) or (p and not q):
                return False
            if p.val != q.val:
                return False
            return check(p.right, q.right) and check(p.left, q.left)
        return check(p,q)

# Time Complexity: O(n + m)
# Space Complexity: O(n + m)
# m is number of nodes in p, n is number of nodes in Q.
