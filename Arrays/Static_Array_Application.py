import array as arr

class Array:

    def __init__(self):
        self.n = 0
        self.capacity = 1
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
        print(f'Length: {n}')
          