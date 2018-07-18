# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        occurrences = {}
        self.findModeHelper(root, occurrences)
        max_value = max(occurrences.values())
        return [k for k, v in occurrences.items() if v == max_value]

    def findModeHelper(self, root, occurrences):
        if root == None:
            return

        if root.val not in occurrences:
            occurrences[root.val] = 1
        else:
            occurrences[root.val] += 1

        self.findModeHelper(root.left, occurrences)
        self.findModeHelper(root.right, occurrences)
