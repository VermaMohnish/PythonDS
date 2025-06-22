class Node:
    def __init__(self,val):
        self.data = val
        self.next = None
       
class Stack:
    def __init__(self):
        self.top = None
    
    def push(self,val):
        new_node = Node(val)
        new_node.next = self.top  
        self.top = new_node       

    def peek(self):
        if self.isempty():
            print("stack is already empty!")
        else :
            return self.top.data
        
        
    def pop(self):
        if self.isempty():
            print("stack is already empty!")
        else :
            temp = self.top
            self.top = self.top.next
            return temp.data
        
    def isempty(self):
        if self.top == None:
            return True
        else :
            return False   
            
            
    def traverse(self):
        temp=self.top
        
        while temp != None :
            print(temp.data)
            temp = temp.next
                        
def main():
    stack = Stack()
    
    print("Pushing elements: 10, 20, 30")
    stack.push(10)
    stack.push(20)
    stack.push(30)
    
    print("\nCurrent stack (top to bottom):")
    stack.traverse()
    
    print("\nTop element (peek):", stack.peek())
    
    print("\nPopping element:", stack.pop())
    
    print("\nStack after pop:")
    stack.traverse()

# Run main
if __name__ == "__main__":
    main()            
            
               
               
        