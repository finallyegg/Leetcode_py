# Design

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from queue import Queue
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        a = set()
        
        ret = []
        q = Queue()
        if not root:
            return ret

        q.put(root)
        while not q.empty():
            node = q.get()
            
            if not node:
                ret.append(None)
                continue

            ret.append(node.val)
            q.put(node.left)
            q.put(node.right)
                
        print(ret)
        return ret
    
    def has_grandChild(self,node:TreeNode):
        if not node:
            return False
        return self.has_child(node.right) or self.has_child(node.left)

    def has_child(self,node:TreeNode):
        if not node:
            return False
        return node.left or node.right
    
    def build_node(self,data):
        if data and data[0]!=None:
            return TreeNode(data.pop(0))
        if len(data):
            data.pop(0)
        return None
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        q = Queue()
        root = self.build_node(data)
        q.put(root)

        while not q.empty():
            node = q.get()
            if node:
                node.left = self.build_node(data)
                node.right = self.build_node(data)
                q.put(node.left)
                q.put(node.right)
            
        print(root)
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))