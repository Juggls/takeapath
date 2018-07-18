import sys


class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        if root.left == None and root.right == None:
            return True

        return (self.isValidBSTHelper(root.left, root.val, -sys.maxsize) and self.isValidBSTHelper(root.right, sys.maxsize, root.val))

    def isValidBSTHelper(self, root, max_val, min_val):
        if root == None:
            return True

        if root.val < max_val and root.val > min_val and root.left == None and root.right == None:
            return True

        if root.val >= max_val or root.val <= min_val:
            return False

        return self.isValidBSTHelper(root.left, root.val, min_val) and self.isValidBSTHelper(root.right, max_val, root.val)
