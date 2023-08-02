class Stack:
    def __init__(self, size):
        self.size = size
        self.array = [None] * size
        self.count = 0

    def stack_size(self):
        return self.count

    def is_empty(self):
        if self.count == 0:
            return True
        else:
            return False

    def push(self, data):
        if self.count == self.size:
            print("Array overloaded")
        else:
            self.array[self.count] = data
            self.count += 1

    def pop(self):
        if self.is_empty() is True:
            return "Array is Empty"
        else:
            self.count -= 1
            return self.array[self.count]

    def peek(self):
        if self.is_empty() is True:
            return "Array is Empty"
        else:
            return self.array[self.count - 1]

    def print_stack(self):
        print(self.array)


S = Stack(3)
S.push(5)
S.push(9)
S.push(4)
S.pop()
print("pick", S.peek())

S.print_stack()
print("Size of the Array:", S.stack_size())
