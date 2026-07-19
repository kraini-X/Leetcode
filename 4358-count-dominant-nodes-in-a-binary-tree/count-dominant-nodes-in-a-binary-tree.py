# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countDominantNodes(self, root: TreeNode | None) -> int:
        ans=0
        def subtreeMax(node):
            nonlocal ans
            if not node:
                #ans+=1
                return float('-inf')
            
            left=subtreeMax(node.left)
            right=subtreeMax(node.right)
            maxVal=max(node.val,left,right)

            if node.val==maxVal:
                ans+=1
            return maxVal
        subtreeMax(root)
        return ans