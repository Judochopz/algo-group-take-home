# implement-stack

I implemented a stack by creating a Node subclass, which contains a value parameter and a next parameter. This allows a node to keep track of its current value as well as the next node in the stack. The stack itself is implemented as a linked-list of these nodes. Without container classes, node objects are the easiest way to implement lists, as elements are easily concatenable and manipulated.

The IntStack class is initialized with an optional list of values to be implemented in the stack, with the last value being the top of the list. Otherwise, the stack begins with no values contained.

The push method takes a given value and creates a node object with it, which is then pushed into the stack as the top element.

The pop method first checks if there is an element (i.e. the top) in the stack. If none, it will throw an error, otherwise it will remove the top node from the stack and return its value.

The peek method first checks if there is an element in the stock. If none, it will throw an error, otherwise it will return the value of the top node in the stack.

The size method first checks that there the top node exists. If not, it returns 0. Otherwise, it iterates through each node of the stack, incrementing the count until it reaches the end of the stack. It then returns the total count of nodes (or values) contained in the stack.
