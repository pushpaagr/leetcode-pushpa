# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
       
       # solved by BST
        # queue = deque()

        # if root:
        #     queue.append(root)
        
        # level = 0
        # while len(queue) > 0:
        #     for i in range(len(queue)):
        #         curr = queue.popleft()
        #         if curr.left:
        #             queue.append(curr.left)
        #         if curr.right:
        #             queue.append(curr.right)
        #     level += 1
        # return level


        # solved by recursion
        if not root:
            return 0
        
        left_depth = 1 + self.maxDepth(root.left)
        right_depth = 1 + self.maxDepth(root.right)
        return max(left_depth, right_depth)





