#class Node:
#    def __init__(self,val):
#        self.data = val
#        self.next = None
    


class Stack:
    def __init__(self):
        self.stack=[]
        
    def push(self,val):
        self.stack.append(val)
    
    def isempty(self):
        if len(self.stack) == 0 :
            return True
        else :
            return False
        
    def pop(self):
        if self.isempty():
            return "Stack is empty"
        else:
            return self.stack.pop()
    
    def peek(self):
        if self.isempty():
            return "Stack is empty"
        else:
            return self.stack[len(self.stack)-1]
    
    def traverse(self):
        for item in reversed(self.stack):
             print(item)
  
  
def main():
    stack = Stack()

    while True:
        print("\nMenu:\n1. Push\n2. Pop\n3. Peek\n4. Traverse\n5. Exit")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if choice == 1:
            try:
                data = int(input("Enter number to push in stack: "))
                stack.push(data)
            except ValueError:
                print("Please enter a valid integer.")
        elif choice == 2:
            print("Popped value:", stack.pop())
        elif choice == 3:
            print("Top value:", stack.peek())
        elif choice == 4:
            print("Stack contents (top to bottom):")
            stack.traverse()
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")
            
main()   
               
       
          
        
                
            
            
        
            
    
