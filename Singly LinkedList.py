# Make a link list of "Hello-->124-->150.45-->20"
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 1

    def length(self):
        print(f"\nTotal nodes {self.count}")

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node
        self.count += 1

    def insert_node(self, node, data):
        new_node = Node(data)
        if node.next is None:
            print("No next Node in the Linked List")
            return
        new_node.next = node.next
        node.next = new_node
        self.count += 1

    def print_node(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data2, end="-->")
            current_node = current_node.next

    def clear(self):
        self.head = None
        self.count = 0

    def delete_head(self):
        if self.head is None:
            print("No size available to delete")
        else:
            self.head = self.head.next
            self.count -= 1

    def delete_tail(self):
        if self.head is None:
            print("Linked List is Empty")
        elif self.head.next is None:
            return self.delete_head()
        else:
            current_node = self.head
            while current_node.next.next is not None:
                current_node = current_node.next
            current_node.next = None
            self.count -= 1

    def remove_value(self, value):
        if self.head is None:
            print("Empty Linked List")
        elif self.head.size == value:
            return self.delete_head()
        else:
            current_node = self.head
            while current_node.next is not None:
                if current_node.next.size == value:
                    break
                current_node = current_node.next
            if current_node.next is None:
                print("Not found")
            else:
                current_node.next = current_node.next.next
                self.count -= 1

    def search(self, value):
        current_node = self.head
        position = 0
        while current_node is not None:
            if current_node.size == value:
                return position
            current_node = current_node.next
            position += 1
        return "Item not found"

    def __getitem__(self, item):
        current_node = self.head
        position = 0
        while current_node is not None:
            if position == item:
                return current_node.size
            current_node = current_node.next
            position += 1
        return "Index Error"

    def replace_with_max(self, value):
        current_node = self.head
        max_data = current_node
        while current_node is not None:
            if current_node.size > max_data.size:
                max_data = current_node
            current_node = current_node.next
        max_data.size = value

    def sum_of_odd_nodes(self):
        current_node = self.head
        counter = 1
        result = 0
        while current_node is not None:
            if counter % 2 == 1:
                result = result + current_node.size

            counter = counter + 1
            current_node = current_node.next
        print(f"Sum of odd nodes: {result}")

    def reverse(self):
        prev_node = None
        current_node = self.head
        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node

        self.head = prev_node


a = LinkedList()
a.add_node(3)
a.add_node(8)
a.add_node(15)
a.add_node(2)

a.print_node()
a.length()
print("-----------Line of control----------")
a.reverse()

a.print_node()
a.length()
