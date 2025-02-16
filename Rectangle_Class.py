class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        # The iteration will return the length first and then the width
        yield {'length': self.length}
        yield {'width': self.width}

# Example usage:
rect = Rectangle(5, 3)

for attribute in rect:
    print(attribute)