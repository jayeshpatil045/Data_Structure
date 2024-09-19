'''

@Author: Jayesh Patil

@Date: 2024-09-18

@Last Modified by: Jayesh Patil

@Title: Queues implementation and problems.

'''
class Node:
    def __init__(self, data):
        """
        Description:
            Initializes a new Node object with the provided data and sets the next pointer to None.

        Parameters:
            data (Any): The data to be stored in the node.

        Returns:
            None
        """
        self.data = data  # Data field
        self.next = None  # Pointer to the next node

class Queue:
    def __init__(self):
        """
        Description:
            Initializes an empty Queue with the front and rear pointers set to None.

        Parameters:
            None

        Returns:
            None
        """
        self.front = None
        self.rear = None

    def is_empty(self):
        """
        Description:
            Checks if the queue is empty.

        Parameters:
            None

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return self.front is None        

    def enqueue(self, value):
        """
        Description:
            Adds a new node with the given value to the end of the queue.

        Parameters:
            value (Any): The data to be added to the queue.

        Returns:
            None
        """
        new_node = Node(value)
        if self.front is None:  
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        """
        Description:
            Removes and returns the node at the front of the queue.

        Parameters:
            None

        Returns:
            Any: The data of the node that was removed if the queue is not empty.
            str: 'Queue empty' if the queue is empty.
        """
        if self.front is None:
            return "Queue empty"
        else:
            data = self.front.data
            self.front = self.front.next
            if self.front is None:  
                self.rear = None
            return data

    def front_item(self):
        """
        Description:
            Returns the data of the node at the front of the queue without removing it.

        Parameters:
            None

        Returns:
            Any: The data of the node at the front if the queue is not empty.
            str: 'Empty queue' if the queue is empty.
        """
        if not self.is_empty():
            return self.front.data
        else:
            return "Empty queue"

    def rear_item(self):
        """
        Description:
            Returns the data of the node at the rear of the queue without removing it.

        Parameters:
            None

        Returns:
            Any: The data of the node at the rear if the queue is not empty.
            str: 'Empty queue' if the queue is empty.
        """
        if not self.is_empty():
            return self.rear.data
        else:
            return "Empty queue"

    def traverse(self):
        """
        Description:
            Traverses and prints the data of each node in the queue from front to rear.

        Parameters:
            None

        Returns:
            None
        """
        temp = self.front
        while temp is not None:
            print(temp.data, end=' ')
            temp = temp.next
        print()

def main():
    """
    Description:
        Demonstrates the functionality of the Queue class by performing various operations on an instance of Queue.
        Operations include enqueueing elements, dequeueing elements, peeking at the front and rear elements,
        and traversing the queue.

    Parameters:
        None

    Returns:
        None
    """
    # Create a Queue instance
    q = Queue()

    # Enqueue elements
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    print("Queue after enqueueing elements:")
    q.traverse()  

    # Peek at the front and rear elements
    print("Front item:")
    print(q.front_item())  
    print("Rear item:")
    print(q.rear_item())  

    # Dequeue elements
    print("Dequeued element:")
    print(q.dequeue()) 
    print("Queue after dequeuing one element:")
    q.traverse() 

    # Check if the queue is empty
    print("Is the queue empty?")
    print(q.is_empty())  

    # Clear the queue
    q.dequeue() 
    q.dequeue() 
    print("Queue after clearing all elements:")
    q.traverse()  

    # Check if the queue is empty again
    print("Is the queue empty?")
    print(q.is_empty())  

if __name__ == "__main__":
    main()

