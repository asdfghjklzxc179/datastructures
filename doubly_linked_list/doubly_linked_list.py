"""
Each Node holds a reference to its prev_panious node
as well as its next_pan node in the List.
"""


class Node:
    def __init__(self, value, prev_pan=None, next_pan=None):
        self.prev_pan = prev_pan
        self.value = value
        self.next_pan = next_pan

    def set_next_pan(self, new_next_pan):
        self.next_pan = new_next_pan
        print(self.next_pan)


"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 1 if self.head is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a Node and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's prev_panious pointer accordingly.
    """

    def add_to_head(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            print(self.head)
        else:
            self.head.prev_pan = new_node
            new_node.next_pan = self.head
            self.head = new_node
            self.length += 1
            print(self.head)

    """
    Removes the List's current head node, making the
    current head's next_pan node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        pass

    """
    Wraps the given value in a Node and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next_pan pointer accordingly.
    """

    def add_to_tail(self, value):
        pass

    """
    Removes the List's current tail node, making the 
    current tail's prev_panious node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        pass

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        pass

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        pass

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        pass


the_double_linked_list = DoublyLinkedList()

the_double_linked_list.add_to_head(1)
print(str(the_double_linked_list.head))
print(str(the_double_linked_list))

the_double_linked_list.add_to_head(2)
print(str(the_double_linked_list.head))
print(str(the_double_linked_list))

the_double_linked_list.add_to_head(7453)
print(str(the_double_linked_list.head))


print(str(the_double_linked_list))
