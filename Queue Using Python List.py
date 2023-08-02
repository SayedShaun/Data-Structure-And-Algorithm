class Queue:
    def __init__(self):
        self.array = []

    def __len__(self):
        return len(self.array)

    def enqueue(self, value):
        self.array.append(value)

    def dequeue(self):
        if len(self.array) == 0:
            raise IndexError("Array is Empty")
        return self.array.pop(0)

    def peek_first(self):
        return self.array[0]

    def peek_last(self):
        return self.array[-1]

    def __str__(self):
        return str(self.array)


q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
print(q)

print(q.dequeue())
print(q.dequeue())

print("This is first item", q.peek_first())
print("This is Last item", q.peek_last())

print("Length ", len(q))
print(q)
