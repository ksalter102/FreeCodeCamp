class Rectangle:

    width = None
    height = None

    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Setters
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    # Calculate area of a rectangle
    def get_area(self):
        return self.width * self.height

    # Calculate perimeter of a rectangle
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    # Calculate diagonal of a rectangle
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    # Get a string with shape of a rectangle
    def get_picture(self):
        # If rectangle is too big
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        # Return a string made of '*' shaped like a rectangle
        return (self.width * '*' + '\n') * self.height

    # Check how many times other shape can fit in this rectangle
    def get_amount_inside(self, other):
        maxw = int(self.width / other.width)
        maxh = int(self.height / other.height)
        return maxw * maxh

    # String representation of a rectangle
    def __str__(self):
        return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"


class Square(Rectangle):

    def __init__(self, length):
        self.width = length
        self.height = length

    # Setters
    def set_side(self, length):
        self.width = length
        self.height = length

    def set_width(self, length):
        self.width = length
        self.height = length

    def set_height(self, length):
        self.width = length
        self.height = length

    # String representation of a square
    def __str__(self):
        return "Square(side=" + str(self.width) + ")"