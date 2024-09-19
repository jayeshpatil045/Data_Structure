'''
@Author: Jayesh Patil
@Date: 2024-09-15
@Last Modified by: Jayesh Patil
@Title: Stack implementation and problems.
'''

class Node:
    def __init__(self, value):
        """
        Description:
            Initializes a new Node object with the provided value and sets the next pointer to None.

        Parameters:
            value (Any): The data to be stored in the node.

        Returns:
            None
        """
        self.data = value  # Data field
        self.next = None  # Pointer to the next node

class Stack:
    def __init__(self):
        """
        Description:
            Initializes the stack with the top element set to None, indicating that the stack is empty.
        
        Parameters:
            None

        Returns:
            None
        """
        self.top = None

    def is_empty(self):
        """
        Description:
            Checks whether the stack is empty.

        Parameters:
            None

        Returns:
            bool: True if the stack is empty, otherwise False.
        """
        return self.top is None

    def push(self, value):
        """
        Description:
            Pushes a new value onto the stack by creating a new node and setting it as the top of the stack.

        Parameters:
            value (Any): The value to be pushed onto the stack.

        Returns:
            None
        """
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def peek(self):
        """
        Description:
            Returns the value of the top element without removing it from the stack.

        Parameters:
            None

        Returns:
            Any: The value of the top element if the stack is not empty.
            str: "Stack is empty" if the stack is empty.
        """
        if self.is_empty():
            return "Stack is empty"
        else:
            return self.top.data

    def pop(self):
        """
        Description:
            Removes and returns the top element from the stack.

        Parameters:
            None

        Returns:
            Any: The value of the top element if the stack is not empty.
            str: "Stack is empty" if the stack is empty.
        """
        if self.is_empty():
            return "Stack is empty"
        else:
            data = self.top.data
            self.top = self.top.next
            return data

    def travers(self):
        """
        Description:
            Traverses the stack and prints each element from top to bottom.

        Parameters:
            None

        Returns:
            None
        """
        temp = self.top
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def size(self):
        """
        Description:
            Calculates and returns the size of the stack by counting the elements.

        Parameters:
            None

        Returns:
            int: The number of elements in the stack.
        """
        temp = self.top
        counter = 0
        while temp is not None:
            temp = temp.next
            counter += 1
        return counter

def reverse_string(string):
    """
    Description:
        Reverses the input string using a stack. Each character of the string is pushed onto the stack,
        and then popped off to form the reversed string.

    Parameters:
        string (str): The string to be reversed.

    Returns:
        None (Prints the reversed string to the console).
    """
    s = Stack()
    for i in string:
        s.push(i)

    res = ""

    while not s.is_empty():
        res = res + s.pop()

    print(res)

def main():
    """
    Description:
        Demonstrates the functionality of the Stack class by performing various operations on an instance of Stack.
        Operations include pushing elements, peeking the top element, popping elements, traversing the stack, and getting the size.
        Also demonstrates reversing a string using the Stack class.

    Parameters:
        None

    Returns:
        None
    """
    # Create a Stack instance
    s = Stack()

    # Push elements onto the stack
    s.push(10)
    s.push(20)
    s.push(30)
    print("Stack after pushing elements:")
    s.travers()  

    # Peek the top element
    print("Top element:")
    print(s.peek())  

    # Pop elements from the stack
    print("Popped element:")
    print(s.pop())  
    print("Stack after popping one element:")
    s.travers()  

    # Get the size of the stack
    print("Size of the stack:")
    print(s.size())  

    # Traverse the stack
    print("Traversing the stack:")
    s.travers()  

    # Reverse a string using the stack
    print("Reversing string 'Jayesh':")
    reverse_string('Jayesh')  

if __name__ == "__main__":
    main()
