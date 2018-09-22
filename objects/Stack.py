class Stack:
    def __init__(self):
        self.data = []

    def __le__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def push(self, item):
        self.data.append(item)
    
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty.")
        return self.data.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty.")
        return self.data[-1]

    def __repr__(self):
        return str([self.data[i] for i in range(len(self.data))])