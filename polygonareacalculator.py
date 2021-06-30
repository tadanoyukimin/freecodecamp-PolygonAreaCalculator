class Rectangle:
    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.side = Square.set_side

    def set_height(self, height):
        self.height = height

    def set_width(self, width):
        self.width = width
    
    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return (self.width * 2) + (self.height * 2)

    def get_diagonal(self):
        return ((self.width ** 2) + (self.height ** 2)) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.width > 50:
            return 'Too big for picture.'
        else:
            return ('*' * self.width + '\n') * self.height

    def get_amount_inside(self, square):
        if self.get_area() >= 1:
            sqarea = Square.get_area(square)
            amountinside = self.get_area() // sqarea
        return amountinside

    def __str__(self):
        return 'Rectangle(width=%d, height=%d)' % (self.width, self.height)

class Square(Rectangle):
    def __init__(self, side, otherside=0):
        super().__init__(side, side)
        self.side = side

    def set_side(self, side):
        self.side = side
    
    def set_height(self, height):
        self.height = height
        self.width = height

    def set_width(self, width):
        self.width = width
        self.height = width

    def __str__(self):
        return 'Square(side=%d)' % (self.side)

rect = Rectangle(8, 16)
sq = Square(6)
sq.set_side(4)
print(sq)
print(sq.set_height(2))
print(sq.get_area())