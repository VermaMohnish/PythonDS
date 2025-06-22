class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self,data):
        self.new_node = Node(data)
        
        if not self.head:
            self.head = self.new_node
            return
        
        last_node = self.head
        
        while last_node.next:
            last_node = last_node.next
        last_node.next = self.new_node
        
    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' ')
            current_node = current_node.next
        print()
        
class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None
        
def main():                 
    ll = LinkedList()
    
    while True:
        try:
            data = int(input("Enter a number to append to the linked list (or 'q' to quit): "))
            ll.append(data)
            ll.display()
            if (input("Do you want to continue? (y/n): ").lower() != 'y'):
                break
            
        except ValueError:
            print("Exiting...")
            break
            print("Please enter a valid integer or 'q' to quit.")
            continue        
    
if __name__ == "__main__":
    main()
