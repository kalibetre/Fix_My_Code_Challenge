#!/usr/bin/python3
"""
User class
"""


class User():
    """ A User Class """

    def __init__(self):
        """ Initializes a user class """
        self.__email = None

    @property
    def email(self):
        """ email of the user """
        return self.__email

    @email.setter
    def email(self, value):
        """ as setter for email of the user """
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value


if __name__ == "__main__":

    u = User()
    u.email = "john@snow.com"
    print(u.email)
