# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def access(self,node, flow):
        i = 0
        while i < len(flow):
            if flow[i] == 'r':
                node = node.right
            else:
                node = node.left
            i+=1
        return node
    
    def f(self,li,node,p): #finds path
    
        if node is p:
            
            return True
        
        if node == None:
            
            return False
    
        righterday = self.f(li,node.right,p)
        if righterday:
            li.append('r')
            
            return True
    
        lefterday = self.f(li,node.left,p)
    
        if lefterday:
            li.append('l')
            return True
        return False
    
    def lowestCommonAncestor(self, root, p, q):
        path1 = []
        path2 = []
        self.f(path1, root,p)
        self.f(path2,root,q)
        path1.reverse()
        path2.reverse()
        
        i = 0
        
        while i < min(len(path1),len(path2)):
            if path1[i] != path2[i]: 
                break
            i+=1
        return self.access(root, path1[:i])
       
            
        
        
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """