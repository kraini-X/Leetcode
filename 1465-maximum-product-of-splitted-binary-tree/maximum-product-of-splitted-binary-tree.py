# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:

        def sums(node):
            if not node:
                return 0
            ans=node.val
            ans+=sums(node.left)
            ans+=sums(node.right)

            return ans
        
        totalSum=sums(root)
        maxm=float('-inf')
        def solve(node):
            nonlocal maxm
            if not node:
                return 0
            
            left=solve(node.left)
            right=solve(node.right)
            subtreeSum=left+node.val+right

            maxm=max(maxm,(totalSum-subtreeSum)*subtreeSum)

            return subtreeSum

        solve(root)
        return maxm%(10**9+7)
            

        