# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def depth(node):
            if not node:
                return 0
            left=1+depth(node.left)
            right=1+depth(node.right)

            return max(left,right)
        
        maxDep=depth(root)

        def solve(node,depth,maxDepth):
            if not node:
                return 0
            
            if not node.left and not node.right and depth==maxDepth:
                return node.val
            
            sums=0
            sums+=solve(node.left,depth+1,maxDepth)
            sums+=solve(node.right,depth+1,maxDepth)

            return sums
        return solve(root,1,maxDep)

            

        