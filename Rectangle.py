#Rectangle class create
class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
    #
    def __iter__(self):
        yield f"Length: {self.length}"
        yield f"Width: {self.width}"

# Example usage
if __name__ == "__main__":
    #user input 
    a = int(input("enter 1st value : "))
    b = int(input("enter 2nd value : "))
    rect = Rectangle(a, b)
    for dimension in rect:
        print(dimension)
