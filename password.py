import string
import secrets

class Password:

    def __init__(self):
        self.__uppers = string.ascii_uppercase
        self.__lowers = string.ascii_lowercase
        self.__numbers = string.digits
        self.__specials = string.punctuation
        self.__length = 16
        self.__charset = ''

    def __str__(self):
        return self.generate()

    def set_charset(self):
        self.__charset = self.__uppers + self.__lowers + self.__numbers + self.__specials
        if len(self.__charset) == 0:
            raise Exception("Error: Your charset is empty")

    def set_length(self, length):
        length = int(length) if length.isnumeric() else 16
        if length < 1:
            length = 1
        if length > 1024:
            length = 1024
        self.__length = length

    def set_uppers(self, uppers):
        self.__uppers = uppers

    def set_lowers(self, lowers):
        self.__lowers = lowers

    def set_numbers(self, numbers):
        self.__numbers = numbers

    def set_specials(self, specials):
        self.__specials = specials

    def generate(self):
        self.set_charset()
        return ''.join(secrets.choice(self.__charset) for i in range(self.__length))
        
    def generate_passphrase(self, length):
        with open('/usr/share/dict/words') as f:
            words = [word.strip() for word in f]
        return ' '.join(secrets.choice(words) for i in range(length))


