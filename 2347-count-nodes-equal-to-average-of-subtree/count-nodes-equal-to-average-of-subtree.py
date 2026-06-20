# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        
        count=0
        def solve(node):
            nonlocal count
            if not node:
                return [0,0]
            
            sums=node.val
            temp=sums
            size=1
            leftSum,leftSize=solve(node.left)
            rightSum,rightSize=solve(node.right)
            sums=sums+leftSum+rightSum
            size=size+rightSize+leftSize

            if temp==(sums//size):
                count+=1
            return [sums,size]
        
        solve(root)
        return count



        