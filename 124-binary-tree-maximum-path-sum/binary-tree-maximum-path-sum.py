# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxm=float('-inf')
        def solve(node):
            nonlocal maxm
            if not node:
                return 0
            left=solve(node.left)
            right=solve(node.right)

            bestLR=node.val+max(left,right)
            curve=left+node.val+right
            single=node.val

            maxm=max(maxm,bestLR,curve,single)

            return max(single,bestLR)
        solve(root)
        return maxm


