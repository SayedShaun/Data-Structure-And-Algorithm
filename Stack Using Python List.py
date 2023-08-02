class Stack:
    def __init__(self):
        self.array = []
        self.count = 0

    def size(self):
        print(self.count)
        return

    def push_item(self, data):
        self.array.append(data)
        self.count += 1

    def pop_item(self):
        if self.count == 0:
            return "Array is Empty"
        else:
            self.array.pop()
            self.count -= 1

    def peek_item(self):
        if self.count == 0:
            return "Array is Empty"
        else:
            return self.array[-1]

    def print(self):
        print(self.array)


S = Stack()
# S.add_item(5)
# S.add_item(6)
# S.add_item(9)
S.pop_item()
print(S.peek_item())
S.print()
S.size()
