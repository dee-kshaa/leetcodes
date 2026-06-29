# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        l=[]
        def preorder(r):
            if not r:
                return
            preorder(r.left)
            preorder(r.right)
            l.append(r.val)
        preorder(root)
        return l
        