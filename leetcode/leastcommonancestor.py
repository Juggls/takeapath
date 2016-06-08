# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def find_path(self, list, node, p):
        if p == node:
            return True
        if not node:
            return False
        if self.find_path(list, node.left, p):
            list.append("l")
            return True
        elif self.find_path(list, node.right, p):
            list.append("r")
            return True
        
        return False
        
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        plist,qlist = [],[]
        
        ppath = self.find_path(plist, root, p)
        qpath = self.find_path(qlist, root, q)
        plist.reverse()
        qlist.reverse()
        
        if p == root and len(qlist) > 0:
            return p
        if q == root and len(plist) > 0:
            return q
        
        count = 0
        pathlist = []
        
        while(count < len(qlist) and count < len(plist)):
            if plist[count] == qlist[count]:
                pathlist.append(plist[count])
                count = count + 1
            else:
                break
            
        
        lca = root
        for step in pathlist:
            if step == "l":
                lca = lca.left
            else:
                lca = lca.right
        
        return lca

   