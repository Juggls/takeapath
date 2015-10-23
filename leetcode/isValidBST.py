# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        tree_array = []
        self.validBSThelper(root, tree_array)
        
        print tree_array
        if sorted(tree_array) == tree_array and not self.is_dups(tree_array):
            return True
        return False
        
    def is_dups(self, x):
        y = {}
        for num in x:
            if num in y:
                return True
            y[num] = True
        return False

        
    def validBSThelper(self, root, tree_array):
        if root == None:
            return
        self.validBSThelper(root.left, tree_array)
        tree_array.append(root.val)
        self.validBSThelper(root.right, tree_array)
        