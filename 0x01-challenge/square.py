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
        if "width" in kwargs:
            self.width = kwargs.get("width")
            self.height = self.width
        elif "height" in kwargs:
            self.height = kwargs.get("height")
            self.width = self.height

    def area_of_my_square(self):
        """ Returns the area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """ Returns the perimeter of a square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ String representation of a square """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
