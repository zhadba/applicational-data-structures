import array as arr

class Array:

    def __init__(self):
        self.capacity = 1
        self.n = 0
        self.array = self.create_array(self.capacity)

    def create_array(self, length):
        return [None] * length

    def show_array(self):
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