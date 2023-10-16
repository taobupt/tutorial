"""python3 program to implement a stack using singly linked list"""
from dataclasses import dataclass


@dataclass
class Node:
    """
    class to create nodes of linked list
    """
    data: any
    next: any = None


class Stack:
    """
    class for the stack data structure
    """

    # head is default NULL
    def __init__(self):
        """
        initialization function
        """
        self.head = None

    def is_empty(self):
        """
        checks if stack is empty
        """
        return self.head is None

    def push(self, data):
        """
        method to add data to the stack
        adds to the start of the stack
        """
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        """
        remove element that is the current head (start of the stack)
        """
        if self.is_empty():
            return None
        # removes the head node and makes
        # the preceding one the new head
        popped_node = self.head
        self.head = self.head.next
        popped_node.next = None
        return popped_node.data

    def peek(self):
        """
        returns the head node data
        """
        if self.is_empty():
            return None
        return self.head.data

    def display(self):
        """
        prints out the stack
        """
        iter_node = self.head
        if self.is_empty():
            print("Stack Underflow")
        else:
            while iter_node is not None:
                print(iter_node.data, end="")
                iter_node = iter_node.next
                if iter_node is not None:
                    print(" -> ", end="")


if __name__ == "__main__":
    my_stack = Stack()

    my_stack.push(11)
    my_stack.push(22)
    my_stack.push(33)
    my_stack.push(44)

    # Display stack elements
    my_stack.display()

    # Print top element of stack
    print("\nTop element is ", my_stack.peek())

    # Delete top elements of stack
    my_stack.pop()
    my_stack.pop()

    # Display stack elements
    my_stack.display()

    # Print top element of stack
    print("\nTop element is ", my_stack.peek())
