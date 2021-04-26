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
            "Custom configuration"            
            ]
    action = Menu.generate(options)

    if action == "1":
        pass
    if action == "2":    
        password.set_uppers("")
        password.set_numbers("")
        password.set_specials("")
    if action == "3":    
        password.set_uppers("")
        password.set_specials("")
    if action == "4":
        custom_password()
    
    if action >= "1" and action <= "4":
        print(password)

if __name__ == "__main__":
    main()
