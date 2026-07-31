# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    from collections import deque
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ""
        ans=[]
        q=deque([root])
        while q:
            for _ in range(len(q)):
                node=q.popleft()

                ans.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return ",".join(map(str, ans))

        
    def insert(self,root,val):
        if not root:
            return TreeNode(val)
        
        if val<root.val:
            root.left=self.insert(root.left,val)
        else:
            root.right=self.insert(root.right,val)
        return root

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None

        vals = list(map(int, data.split(',')))

        root=None

        for val in vals:
            root=self.insert(root,val)
        return root


        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans