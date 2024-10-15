class Stack:
    def __init__(self):
        self.stack = []
        
    # Check if the stack is empty
    def empty(self):
        return len(self.stack) == 0
    
    # Add an element to the stack(PUSH)
    def push(self, item):
        self.stack.append(item)
        
    # Remove an element from the stack(PULL)
    def pull(self):
        if self.empty():
            return "Stack is Empty"
        return self.stack.pop()
        
    # Peek the top of the stack(NO REMOVAL)
    def peek(self):
        if self.empty():
            return "Stack is Empty"
        return self.stack[-1]
        
    # Return the size of the stack
    def size(self):
        return len(self.stack)
    
    # Display the elements of the stack
    def display(self):
        return self.stack
    
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print("Printing the Stack: ", stack.display())
stack.pull()
print("Check the top element of the Stack: ", stack.peek())