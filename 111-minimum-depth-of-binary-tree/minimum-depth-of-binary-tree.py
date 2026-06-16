# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        #minDepth=float('inf')
        def solve(node,depth):
            if not node:
                return 0
            if not node.left and not node.right:
                return depth
            #minDepth=min(minDepth,depth)
            left=solve(node.left,depth+1)
            right=solve(node.right,depth+1)
            if left==0:
                return right
            elif right==0:
                return left
            return min(left,right)
        return solve(root,1)
            

        