userInput = input("Choose your password: ")

def isValid(password):

    if(len(password) > 5 and len(password) < 15):

        lowerCase = False
        upperCase = False
        num = False
        special = False

        for char in password:
            if(char.isdigit()):
                num = True
            else:
                print("At least one number is required. ")

            if(char.islower()):
                lowerCase = True
            else:
                print("At least one lowercase letter is required. ")

            if(char.isupper()):
                upperCase = True
            else:
                print("At least one uppercase letter is required. ")

            if(not char.isalnum()):
                special = True
            else:
                print("At least one special character is required. ")

        return "Valid password. "

    else:
        return "Password must be between the length of 6 and 14. "

print(isValid(userInput))
