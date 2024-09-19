'''

@Author: Jayesh Patil

@Date: 2024-09-15

@Last Modified by: Jayesh Patil

@Title: Linked List Problems

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
        self.data = data  
        self.next = None  

class LinkedList:
    def __init__(self):
        """
        Description:
            Initializes an empty LinkedList with the head set to None and node count (n) set to 0.

        Parameters:
            None

        Returns:
            None
        """
        self.head = None  
        self.n = 0  

    def __len__(self):
        """
        Description:
            Returns the number of nodes in the LinkedList.

        Parameters:
            None

        Returns:
            int: The number of nodes in the LinkedList.
        """
        return self.n

    def insert_head(self, value):
        """
        Description:
            Inserts a new node with the given value at the head (beginning) of the LinkedList.

        Parameters:
            value (Any): The data to be inserted at the head.

        Returns:
            None
        """
        new_node = Node(value)
        new_node.next = self.head  
        self.head = new_node  
        self.n += 1

    def __str__(self):
        """
        Description:
            Returns a string representation of the LinkedList, with nodes displayed as 'data->data'.

        Parameters:
            None

        Returns:
            str: A string showing all node values in sequence.
        """
        curr = self.head
        result = ''
        while curr is not None:
            result += str(curr.data) + '->'
            curr = curr.next
        return result[:-2]  

    def append(self, value):
        """
        Description:
            Appends a new node with the given value to the end of the LinkedList.

        Parameters:
            value (Any): The data to be appended.

        Returns:
            None
        """
        new_node = Node(value)
        if self.head is None:  
            self.head = new_node
            self.n += 1
            return
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = new_node
        self.n += 1

    def insert_after(self, after, value):
        """
        Description:
            Inserts a new node with the given value after the node that contains the 'after' value.

        Parameters:
            after (Any): The value after which the new node is to be inserted.
            value (Any): The value to be inserted into the new node.

        Returns:
            str: 'Item not found' if the node with 'after' value is not found, otherwise None.
        """
        new_node = Node(value)
        curr = self.head
        while curr is not None:
            if curr.data == after:
                break
            curr = curr.next
        if curr is not None:
            new_node.next = curr.next
            curr.next = new_node
            self.n += 1
        else:
            return 'Item not found'

    def clear(self):
        """
        Description:
            Clears the LinkedList by resetting the head to None and node count to 0.

        Parameters:
            None

        Returns:
            None
        """
        self.head = None
        self.n = 0

    def delete_head(self):
        """
        Description:
            Deletes the head node of the LinkedList.

        Parameters:
            None

        Returns:
            str: 'Empty LinkedList' if the list is already empty, otherwise None.
        """
        if self.head is None:  # Empty list case
            return 'Empty LinkedList'
        self.head = self.head.next
        self.n -= 1

    def pop(self):
        """
        Description:
            Removes and returns the last element of the LinkedList.

        Parameters:
            None

        Returns:
            str: 'Empty LinkedList' if the list is empty, otherwise None.
        """
        if self.head is None:  
            return 'Empty LinkedList'
        curr = self.head
        if curr.next is None:
            return self.delete_head()
        while curr.next.next is not None:
            curr = curr.next
        curr.next = None
        self.n -= 1

    def remove(self, value):
        """
        Description:
            Removes the first occurrence of the node with the given value from the LinkedList.

        Parameters:
            value (Any): The value of the node to be removed.

        Returns:
            str: 'Empty LinkedList' if the list is empty, 'Not Found' if the value is not found, otherwise None.
        """
        if self.head is None:
            return 'Empty LinkedList'
        if self.head.data == value:
            return self.delete_head()
        curr = self.head
        while curr.next is not None:
            if curr.next.data == value:
                break
            curr = curr.next
        if curr.next is None:
            return 'Not Found'
        else:
            curr.next = curr.next.next
            self.n -= 1

    def search(self, item):
        """
        Description:
            Searches for the given item in the LinkedList and returns its position.

        Parameters:
            item (Any): The value to search for in the LinkedList.

        Returns:
            int: The position of the item if found.
            str: 'Not Found' if the item is not found.
        """
        curr = self.head
        pos = 0
        while curr is not None:
            if curr.data == item:
                return pos
            curr = curr.next
            pos += 1
        return 'Not Found'

    def __getitem__(self, index):
        """
        Description:
            Returns the data of the node at the specified index.

        Parameters:
            index (int): The position of the node to retrieve.

        Returns:
            Any: The data of the node at the specified index.
            str: 'IndexError' if the index is out of bounds.
        """
        curr = self.head
        pos = 0
        while curr is not None:
            if pos == index:
                return curr.data
            curr = curr.next
            pos += 1
        return 'IndexError'
def main():
    """
    Description:
        Demonstrates the functionality of the LinkedList class by performing various operations on an instance of LinkedList.
        Operations include inserting nodes, appending nodes, inserting after a specific node, removing nodes, and more.

    Parameters:
        None

    Returns:
        None
    """
    ll = LinkedList()

    ll.insert_head(10)
    ll.insert_head(20)
    ll.insert_head(30)
    print("LinkedList after inserting at the head:")
    print(ll)  

    ll.append(40)
    ll.append(50)
    print("LinkedList after appending nodes:")
    print(ll)  

    ll.insert_after(20, 25)
    print("LinkedList after inserting 25 after 20:")
    print(ll)  

    print("Search for value 25:")
    print(ll.search(25))  

    ll.remove(10)
    print("LinkedList after removing node with value 10:")
    print(ll) 

    ll.delete_head()
    print("LinkedList after deleting the head node:")
    print(ll)  

    ll.pop()
    print("LinkedList after popping the last node:")
    print(ll)  

    # Get the data at a specific index
    print("Data at index 1:")
    print(ll[1])  

    # Clear the LinkedList
    ll.clear()
    print("LinkedList after clearing:")
    print(ll)  

if __name__ == "__main__":
    main()
