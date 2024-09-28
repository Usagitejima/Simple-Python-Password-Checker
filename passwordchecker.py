userInput = input("Choose your password: ")
validPass = False

def isValid(password):

        lowerCase = False
        upperCase = False
        num = False
        special = False

        for char in password:
            if(char.isdigit()):
                num = True

            if(char.islower()):
                lowerCase = True

            if(char.isupper()):
                upperCase = True

            if(not char.isalnum()):
                special = True

        if (num == False or lowerCase == False or upperCase == False or special == False):
            if (num == False):
                print("At least one number is required. ")
            if(lowerCase == False):
                print("At least one lowercase letter is required. ")
            if(upperCase == False):
                print("At least one uppercase letter is required. ")
            if(special == False):
                print("At least one special character is required. ")
        else:
            print("Valid password.")


while (validPass == False):

    if (len(userInput) > 5 and len(userInput) < 15):
        validPass = True
        print(isValid(userInput))
    else:
        print("Password must be between the length of 6 and 14.")
        userInput = input("Choose your password: ")

