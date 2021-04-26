from menu import Menu
from password import Password

password = Password()

def custom_password():
    print()
    print("Set your password length")
    password.set_length(input("Length: "))
    print()

    print("Set your charset, press enter to skip an option")
    password.set_uppers(input("Uppers: "))
    password.set_lowers(input("Lowers: "))
    password.set_numbers(input("Numbers: "))
    password.set_specials(input("Specials: "))
    print()

def main():
    print("Create a password")

    options = [
            "Default configuration", 
            "Only lower letters",
            "Lower letters and numbers",
            "Custom configuration",
            "Four random common words"            
            ]
    action = Menu.generate(options)

    if action == "1":
        print(password.generate())
    if action == "2":    
        password.set_uppers("")
        password.set_numbers("")
        password.set_specials("")
        print(password.generate())
    if action == "3":    
        password.set_uppers("")
        password.set_specials("")
        print(password.generate())
    if action == "4":
        custom_password()
        print(password.generate())  
    if action == "5":
        print(password.generate_passphrase(4))

if __name__ == "__main__":
    main()
