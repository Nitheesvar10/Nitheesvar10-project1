class myQueue:

    def __init__(self):
        self.stack1=[]
        self.stack2=[]
        # Initialize your data members
        

    def enqueue(self, x):
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(x)
        while self.stack2:
            self.stack1.append(self.stack2.pop())
            
        # Implement the enqueue operation
        
        
    def dequeue(self):
        if not self.stack1:
            return -1
        return self.stack1.pop()
        # Implement the dequeue operation


    def front(self):
        if not self.stack1:
            return -1
        return self.stack1[-1]
        # Return the front element of the queue


    def size(self):
        return len(self.stack1)
        # Return the current size of the queue