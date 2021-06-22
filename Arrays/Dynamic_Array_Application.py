import array as arr

class Array: #all methods use print instead of return, just to increase simplicity

    def __init__(self):
        self.capacity = 1
        self.n = 0
        self.array = self.create_array(self.capacity)
        
    def create_array(self, length): #can be updated to accept user based values if necessary
        return [None] * length

    def resize_array(self, new_capacity):
        new_array = self.create_array(new_capacity)

        for i in range(self.n):
            new_array[i] = self.array[i]

        self.array = new_array
        self.capacity = new_capacity

    def show_array(self): #applicable to small data sets
        count = 0
        for item in self.array:
            print(f'Index: {count} --> Item: {item}')
            count += 1

    def get_length(self):
        n = len(self.array)
        return n

    def print_length(self):
        self.n = self.get_length()
        print(f'Length: {self.n}')

    def get_index(self, index):
        self.n = self.get_length()
        if not 0 <= index < self.n:
            print('Error: invalid index')
        else:
            print(f'Index: {index} --> Item: {self.array[index]}')

    def append_item(self, item):
        if self.n == self.capacity:
            self.resize_array(2 * self.capacity)

        self.array.append(item)
        self.n += 1

        self.show_array()

    def insert_item(self, item, index):
        if self.n == self.capacity:
            self.resize_array(2 * self.capacity)

        if 0 <= index < self.n:
            self.array.insert(index, item)
            self.show_array()
        else:
            print('Error: invalid index')

    def remove_item(self, index):
        self.n = self.get_length()
        if self.n == 0:
            print('Error: cannot remove item from empty array')
        else:
            del self.array[index]

Array().get_index(0)