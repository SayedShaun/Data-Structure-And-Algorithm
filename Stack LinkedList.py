class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.count = 0

    def size(self):
        print(f"\nTotal Nodes are: {self.count}")

    def push(self, data):
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.count += 1

    def pop(self):
        if self.top is None:
            raise IndexError("Stack is Empty")
        else:
            data = self.top.size
            self.top = self.top.next
            return data
        self.count -= 1

    def peek(self):
        if self.top is None:
            print("Stack is Empty")
        else:
            data = self.top.size
            print(f"This is peek Node: {data}")
        self.count -= 1

    def is_empty(self):
        return self.top is None

    def print(self):
        current_node = self.top
        while current_node is not None:
            print(current_node.size)
            current_node = current_node.next


def reverse(text):
    for i in text:
        S.push(i)

    result = ""
    while S.is_empty() is not None:
        result += S.pop()
    print(result)


S = Stack()
S.push(5)
S.push(7)
S.push(20)
S.print()
print("-----------------------------------")
S.pop()
S.print()
S.size()
