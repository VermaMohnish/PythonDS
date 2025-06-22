class queue:
    def __init__(self):
        self.queue=[]
        
    def push(self,val):
        self.queue.insert(0,val)
    
    def isempty(self):
        if len(self.queue) == 0 :
            return True
        else :
            return False    
        
    def pop(self):
        if self.isempty():
            return "Stack is empty"
        else:
            return self.queue.pop()    
        
    def traverse(self):
        for item in (self.queue):
             print(item)
        
def main():
    q = queue()
    
    print("Pushing elements: 10, 20, 30")
    q.push(10)
    q.push(20)
    q.push(30)

    print("\nQueue after pushes (front to back):")
    q.traverse()  # Shows: 30, 20, 10

    print("\nPopping element:", q.pop())  # Should remove 10 (back of list)
    
    print("\nQueue after one pop:")
    q.traverse()  # Shows: 30, 20

    print("\nIs queue empty?", q.isempty())  # Should be False

# Run main
if __name__ == "__main__":
    main()        