class bst :
    def __init__(self) :
        self.root = None
    
    def insert(self,root,value) :
        
        if root is None :
            return Node(value)
        elif value < root.data :
            root.left = self.insert(root.left,value)
        elif value > root.data :
            root.right = self.insert(root.right,value)
        
        return root
    
    def preorder(self,root) :
        if root is not None :
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)
        
    def inorder(self,root) :
        if root is not None :
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)
            
    def postorder(self,root) :
        if root is not None :
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data)        
                 
    def delete(self,root,key) :
        
        if root is None :
            return None
        elif root.data > key :
            root.left = self.delete(root.left,key)
        elif root.data < key :
            root.right = self.delete(root.right,key)
        else :
            if root.left is None :
                return root.right
            elif root.right is None :
                return root.left
        
        root.data = findrep(root.left)
        root.left = self.delete(root.left,root.data)
        
        return root
                     

def findrep(leftroot) : 
    while leftroot.right is not None :
        leftroot = leftroot.right
    return leftroot.data
                   
class Node :
    def __init__ (self, val : int) :
        self.data = val
        self.left = None
        self.right = None
        
def main() :
    tree = bst()
    values = [50, 30, 70, 20, 40, 60, 80]
    for val in values:
        tree.root = tree.insert(tree.root, val)

    print("Inorder traversal:")
    tree.inorder(tree.root)
    print("\nPreorder traversal:")
    tree.preorder(tree.root)
    print("\nPostorder traversal:")
    tree.postorder(tree.root)

    print("\n\nDeleting node 50...")
    tree.root = tree.delete(tree.root, 50)

    print("Inorder after deletion:")
    tree.inorder(tree.root)

if __name__ == "__main__":
    main()
    
                        