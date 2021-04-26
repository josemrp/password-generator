from random import shuffle

class Password:
    __uppers = []
    __lowers = []
    __numbers = []
    __specials = []
    __length = 0
    __charset = []

    def __init__(self):
        self.__uppers = [chr(i) for i in range(ord("A"), ord("Z"))]
        self.__lowers = [chr(i) for i in range(ord("a"), ord("z"))]
        self.__numbers = [str(i) for i in range(10)]
        self.__specials = list("!#$%&/()=?+*[];:_,.-{}")
        self.__length = 16

    def __str__(self):
        return self.generate()

    def set_charset(self):
        self.__charset = self.__uppers + self.__lowers + self.__numbers + self.__specials
        if len(self.__charset) < self.__length:
            try:
                mult = self.__length / len(self.__charset)
                self.__charset *= int(mult) + 1
            except ZeroDivisionError:
                print("Error: Your charset is empty")
        shuffle(self.__charset)

    def set_length(self, length):
        length = int(length) if length.isnumeric() else 16
        if length < 1:
            length = 1
        if length > 1024:
            length = 1024
        self.__length = length

    def set_uppers(self, uppers):
        self.__uppers = [str(i) for i in uppers]

    def set_lowers(self, lowers):
        self.__lowers = [str(i) for i in lowers]

    def set_numbers(self, numbers):
        self.__numbers = [str(i) for i in numbers]

    def set_specials(self, specials):
        self.__specials = [str(i) for i in specials]

    def generate(self):
        self.set_charset()
        return ''.join(self.__charset[:self.__length])

