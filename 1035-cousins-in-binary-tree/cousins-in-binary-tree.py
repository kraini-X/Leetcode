# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        from collections import deque
        q = deque([(root, None)])

        while q:
            px=None
            py=None
            FoundX=False
            FoundY=False
            for _ in range(len(q)):
                node,parent=q.popleft()

                if node.val==x:
                    FoundX=True
                    px=parent

                if node.val==y:
                    FoundY=True
                    py=parent
                
                if node.left:
                    q.append((node.left,node))
                
                if node.right:
                    q.append((node.right,node))
                
            
            if FoundX and FoundY:
                return px!=py 
            
            if FoundX or FoundY:
                return False

        