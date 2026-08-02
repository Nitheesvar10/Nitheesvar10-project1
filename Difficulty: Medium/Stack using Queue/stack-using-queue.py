from collections import deque


class myStack:

    def __init__(self):
        self.q = deque()

    def push(self, x):
        # push element on top
        self.q.append(x)
        # Implement the enqueue operation
        for _ in range(len(self.q)-1):
            self.q.append(self.q.popleft())
        
    def pop(self):
        if not self.q:
            return -1
        return self.q.popleft()
        # remove top element
        
    def top(self):
        if not self.q:
            return -1
        return self.q[0]
        # return top element
        
    def size(self):
        return len(self.q)
        # return current size
        
