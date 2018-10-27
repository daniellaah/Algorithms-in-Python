"""113. Path Sum II
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ret, path = [], []
        self.findPath(root, sum, path, ret)
        return ret

    def findPath(self, node, sum, path, ret):
        path.append(node.val)
        if node.val == sum and not node.left and not node.right:
            ret.append(path[:])
        if node.left:
            self.findPath(node.left, sum-node.val, path, ret)
        if node.right:
            self.findPath(node.right, sum-node.val, path, ret)
        path.pop()
