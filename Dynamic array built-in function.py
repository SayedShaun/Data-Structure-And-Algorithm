class DynamicArray:
    def __init__(self):
        self.array = []

    def add_element(self, element):
        self.array.append(element)

    def remove_element(self, element):
        self.array.remove(element)

    def get_array(self):
        return self.array

    def set_array(self):
        pass


result = DynamicArray()
result.add_element(1)
result.add_element(2)
result.add_element("Hello")
result.remove_element(2)
print(result.array)
