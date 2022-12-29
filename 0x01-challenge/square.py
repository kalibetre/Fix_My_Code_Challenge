#!/usr/bin/python3
"""
square module contains
    - square class
"""


class Square():
    """
    Square class
    """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """
        Initializes a square
        """
        for key, value in kwargs.items():
            setattr(self, key, value)
        if "width" in kwargs and self.width != self.height:
            self.height = self.width
        if "height" in kwargs and self.width != self.height:
            self.width = self.height
        if self.width < 0:
            self.width = self.height = 0

    def area_of_my_square(self):
        """ Returns the area of the square """
        return self.width * self.height

    def permiter_of_my_square(self):
        """ Returns the perimeter of a square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ String representation of a square """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ Tests the Square class"""
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
    s = Square(width=12)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
    s = Square(height=12)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
    s = Square()
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
    s = Square(12)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
