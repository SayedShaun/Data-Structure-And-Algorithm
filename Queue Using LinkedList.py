class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0

    def queue_size(self):
        return self.count

    def enqueue(self, value):
        new_node = Node(value)
        if self.front is None:
            self.front = new_node
            self.rear = self.front

        else:
            self.rear.next = new_node
            self.rear = new_node

        self.count += 1

    def dequeue(self):
        if self.front is None:
            return "Queue is Empty"
        else:
            self.front = self.front.next

        self.count -= 1

    def peek_first(self):
        if self.front is None:
            return "Queue is Empty"
        else:
            return self.front.size

    def peek_last(self):
        if self.front is None:
            return "Queue is Empty"
        else:
            return self.rear.size

    def print_queue(self):
        current_node = self.front
        while current_node is not None:
            print(current_node.size, end="->")
            current_node = current_node.next


Q = Queue()
Q.enqueue(5)
Q.enqueue(9)
Q.enqueue("Hello")

print(Q.peek_first())
print(Q.peek_last())
Q.print_queue()
print("\nQueue size", Q.queue_size())
