# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:       
    def deleteNode(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if val > root.val:
            root.right = self.deleteNode(root.right, val)
        elif val < root.val:
            root.left = self.deleteNode(root.left, val)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            # find the min from the right subtree
            curr = root.right
            while curr and curr.left:
                curr = curr.left
            root.val = curr.val
            root.right = self.deleteNode(root.right, root.val)
        return root

             
             


