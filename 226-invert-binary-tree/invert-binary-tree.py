# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        elif root.left == None and root.right == None:
            return root
        else:
            queue = deque([root])
            while queue:
                node = queue.popleft()
                temp = 0
                if not node:
                    continue
                temp = node.left
                node.left = node.right
                node.right = temp
                queue.append(node.left)
                queue.append(node.right)
        return root

                
        
        