class Node:
    def __init__(self, value, pointer_to_next_node_and_also_the_new_node=None):
        self.value = value
        self.pointer_to_next_node_and_also_the_new_node = pointer_to_next_node_and_also_the_new_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.pointer_to_next_node_and_also_the_new_node

    def set_pointer_to_next_node_and_also_the_new_node(self, new_pointer_to_next_node_and_also_the_new_node):
        self.pointer_to_next_node_and_also_the_new_node = new_pointer_to_next_node_and_also_the_new_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.tail = new_node
            self.head = new_node
        else:
            # current tail's pointer is set to the new node
            self.tail.pointer_to_next_node_and_also_the_new_node = new_node
            # the new tail is now the new node
            self.tail = new_node

    def remove_tail(self):
        if self.head is None and self.tail is None:
            return None
        if self.tail == self.head:
            value = self.tail.get_value()
            self.tail = None
            self.head = None
            return value
        else:
            value = self.tail.get_value()
            current_node = self.head
            while current_node.get_next() != self.tail:
                current_node = current_node.get_next()
            self.tail = current_node
            self.tail.set_pointer_to_next_node_and_also_the_new_node(None)
            return value

    def add_to_head(self, value):
        new_node = Node(value)
        if self.tail is None and self.head is None:
            self.tail = new_node
            self.head = new_node
        else:
            new_node.pointer_to_next_node_and_also_the_new_node = self.head
            self.head = new_node

    def remove_head(self):
        if self.head is None and self.tail is None:
            return None
        if self.head == self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value
        else:
            value = self.head.get_value()
            self.head = self.head.get_next()
            return value

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next
    # def set_previous?

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
