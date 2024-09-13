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



    else:
        return "Password must be between the length of 6 and 14. "

print(isValid(userInput))
