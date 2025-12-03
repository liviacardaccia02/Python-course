
# A class for stacks
class Stack(object):

    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop() if not self.is_empty() else None

    def peek(self):
        return self.stack[-1] if not self.is_empty() else None

    def clear(self):
        self.stack = []

    def is_empty(self):
        return self.size() == 0

    def __str__(self):
        return str(self.stack)

