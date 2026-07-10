# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        #0-noCam
        #1-hasCam
        #2-covered
        if not root.left and not root.right:
            return 1
        cameras=0
        def solve(node):
            nonlocal cameras
            if not node:
                return 2
            
            left=solve(node.left)
            right=solve(node.right)

            if left==0 or right==0:
                cameras+=1
                return 1
            
            elif left==1 or right==1:
                return 2
            
            else:
                return 0
        if solve(root)==0:
            cameras+=1
        return cameras


        