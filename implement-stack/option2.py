# OPTION 2 - IMPLEMENT STACK
# DO NOT SHARE

# 2. Implement a growable integer stack (without using container libraries like vector, list, etc.)
#    that satisfies the following requirements:

# `push` adds a given value to the top
# `pop`  returns and removes the value at the top
# `peek` returns the value at the top
# `size` returns the count of values

class IntStack:
    class Node:
        # Node class to as element in stack
        
        def __init__(self, value):
            self.value = value
            self.next = None

        def add_node(self, node):
            self.next = node
    
    def __init__(self, values=None):
        self.top = None
        if values:
            if type(values) != list:
                raise Exception("You must provide values in the form of a list or None")
            for value in values:
                cur = IntStack.Node(value)
                if self.top:
                    cur.add_node(self.top)
                self.top = cur
    
    def push(self, value):
        cur = IntStack.Node(value)
        cur.add_node(self.top)
        self.top = cur
        return None
    
    def pop(self):
        if not self.top:
            raise Exception("There is nothing in the stack.")

        result = self.top.value
        new = self.top.next
        self.top = new
        return result
    
    def peek(self):
        if not self.top:
            raise Exception("There is nothing in the stack.")
        
        return self.top.value
    
    def size(self):
        if not self.top:
            return 0
        
        cur = self.top
        count = 0
        while cur:
            count += 1
            cur = cur.next
        
        return count
    
