'''Double Ended Queue'''

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_left(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def push_right(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def pop_left(self):
        if self.head is None:
            return None
        data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
        return data

    def pop_right(self):
        if self.tail is None:
            return None
        data = self.tail.data
        self.tail = self.tail.prev
        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None
        return data

    def print_deque(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next


d = Deque()
d.push_right("B")
d.push_right("C")
d.push_left("A")

print("Deque:")
d.print_deque()
print("pop_left:", d.pop_left())
print("pop_right:", d.pop_right())
print("Deque ahora:")
d.print_deque()
print("pop_right:", d.pop_right())
print("pop_right (vacío):", d.pop_right())
print("pop_left (vacío):", d.pop_left())
print("head y tail:", d.head, d.tail)