
class Node:
    def __init__(self, value, prev_pan=None, next_pan=None):
        self.prev_pan = prev_pan
        self.value = value
        self.next_pan = next_pan

    def set_next_pan(self, new_next_pan):
        self.next_pan = new_next_pan
        print(self.next_pan)

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_pan

    def get_prev(self):
        return self.prev_pan

    def get_node(self, node):
        while node is not None:
            if node == self.value:
                return node


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
            print(self.length)

        else:
            self.head.prev_pan = new_node
            new_node.next_pan = self.head
            self.head = new_node
            self.length += 1
            print(self.head)
            print(self.length)

    """
    Removes the List's current head node, making the
    current head's next_pan node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        if self.head is None and self.tail is None:
            return None
        if self.head == self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            self.length -= 1
            print(self.length)

            return value

        else:
            value = self.head.get_value()
            self.head = self.head.get_next()
            self.length -= 1
            print(self.length)

            return value

    """
    Wraps the given value in a Node and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next_pan pointer accordingly.
    """

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.tail is None:
            self.tail = new_node
            self.head = new_node
            self.length -= 1
            print(self.tail)
            print(self.length)

        else:
            self.tail.next_pan = new_node
            new_node.prev_pan = self.tail
            self.tail = new_node
            self.length += 1
            print(self.tail)
            print(self.length)

    """
    Removes the List's current tail node, making the 
    current tail's prev_panious node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        if self.head is None and self.tail is None:
            return None
        if self.head == self.tail:
            value = self.tail.get_value()
            self.head = None
            self.tail = None
            self.length -= 1
            print(self.length)

            return value

        else:
            value = self.tail.get_value()
            self.tail = self.tail.get_prev()
            self.tail.next_pan = None
            print(self.tail.get_next())
            self.tail.prev_pan = self.tail.get_prev()
            self.next_pan = self.tail.prev_pan
            self.length -= 1
            print(self.length)

            return value

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        new_front = Node(node).get_node()
        old_front = self.head
        self.head.prev_pan = new_front
        self.head = new_front
        self.head.next_pan = old_front
        print(self.head)
        print(new_front)
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
print(str(the_double_linked_list))

the_double_linked_list.add_to_head(2)
print(str(the_double_linked_list))

the_double_linked_list.add_to_head(7453)
print(str(the_double_linked_list))

the_double_linked_list.remove_from_head()

print(str(the_double_linked_list))
print(str(the_double_linked_list.head))

the_double_linked_list.move_to_front(2)
