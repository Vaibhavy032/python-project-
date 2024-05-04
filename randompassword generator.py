#Random Password Generator-     


import string
import random

print()
print("Name: Vaibhav Yadav")
print("SAP ID: 500122758")
print("RollNO.: R2142231471")
print()
print("Topic: :Password Generator: ")
print()

print("Do you want to insert your own password?")
choice = str(input("Enter Y for custom password and N for auto generated password: "))

if choice == 'N' or choice == 'n':
    def generate_password(passlen):
        str1 = string.ascii_lowercase
        str2 = string.ascii_uppercase
        str3 = string.digits
        str4 = string.punctuation

        str = yields
        str.extend(list(str1))
        str.extend(list(str2))
        str.extend(list(str3))
        str.extend(list(str4))

        # will generate a random password
        password = "".join(random.sample(str, passlen))
        return password
  
    passlen = int(input("Enter password length: "))
    password = generate_password(passlen)

    # Will write the password to a file
    with open("passwords.txt", "a") as file:
        file.write(password + "\n")

    print(f"Your password is: {password}")
    print("Password saved to passwords.txt")


elif choice == 'Y' or choice == 'y':
    password=str(input("Enter custom password: "))
     # Writing the password to a file
    with open("passwords.txt", "w") as file:
        file.write(password + "\n")

    print(f"Your password is: {password}")
    print("Password saved to passwords.txt")

else:
    print("Wrong input!!!")

print("Thank You For Using!!!")





