# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n=len(inorder)
        idx=0

        def solve(start,end):
            nonlocal idx
            if start>end:
                return
            
            root=TreeNode(preorder[idx])
            j=0
            for i in range(n):
                if preorder[idx]==inorder[i]:
                    j=i
                    break
            idx+=1
            root.left=solve(start,i-1)
            root.right=solve(i+1,end)

            return root
        return solve(0,n-1)


        