class Menu:
    
    @staticmethod
    def generate(options):
        i = 1
        for option in options:
            print("{i}. {option}".format(i=i, option=option))
            i += 1

        return input("Select an option: ")





