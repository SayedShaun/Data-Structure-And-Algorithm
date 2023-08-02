class Queue:
    def __init__(self, size):
        self.size = size
        self.array = [None] * self.size
        self.count = 0

    def __len__(self):
        return self.count

    def enqueue(self, value):
        if self.count == self.size:
            raise IndexError("Queue is Overloaded")
        self.array[self.count] = value
        self.count += 1

    def dequeue(self):
        if self.count == 0:
            raise IndexError("Queue is Empty")
        self.count -= 1

        first_item = self.array[0]
        self.array = self.array[1:]
        return first_item

    def peek_first(self):
        if self.count == 0:
            raise IndexError("Queue is Empty")
        return self.array[0]

    def peek_last(self):
        if self.count == 0:
            raise IndexError("Queue is Empty")
        return self.array[-1]

    def __str__(self):
        return str(self.array)


q = Queue(7)

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