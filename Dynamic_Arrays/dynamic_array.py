"""
So already has a built in dynamic array that auto grows and shrinks.
This is just to see how static arrays could be made into a dynamic arrays.
"""


class DynamicArray:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.size = 0

    def add(self, n: int):
        if self.size == self.capacity:
            self.increase_capacity()
        self.array[self.size] = n
        self.size += 1

    def increase_capacity(self):
        self.capacity *= 2
        temp_array = [None] * self.capacity
        for i in range(self.size):
            temp_array[i] = self.array[i]
        self.array = temp_array

    def get_array(self):
        return self.array

    # A function to insert item in a specific index of the array.

da = DynamicArray(2)
da.add(1)
da.add(2)
da.add(3)
print(da.get_array())
