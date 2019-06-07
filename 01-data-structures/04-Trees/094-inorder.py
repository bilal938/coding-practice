#Definition for a binary tree node.
#Given a binary tree, return the inorder traversal of its nodes' values.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def traverse(root, lis):
        if root != null:
            if root.left != null:
                traverse(root.left, lis)
            lis.append(root.val)
            if root.right != null:
                traverse(root.right, lis)
            
            
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        lis = []
        traverse(root, lis)
        return lis
