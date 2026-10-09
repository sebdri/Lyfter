'''STACK'''



class Node:
    def __init__(self,data):
        self.data = data
        self.next = Node



class stack:
    def __init__(self):
        self.top = None


    def push(self,data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if Node is None:
            return None
        data = self.top
        self.top = self.top.next
        return data



    def print_stack(self):
        current = self.top
        while current is not None:
            print(current.data)
            current = current.next




s=stack()
s.push("Taekwondo")
s.push("MMA")
s.push("Surf")

s.print_stack()