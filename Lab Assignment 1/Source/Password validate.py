import re

# Initial display of the application
print("\nWelcome to My UMKC web application for password updation \n")
print("Criteria for a Valid password:\n"
      "1) The password length should be in range 6-16 characters \n"
      "2) Should have atleast one number \n"
      "3) Should have atleast one special character in [$@!*] \n"
      "4) Should have atleast one lowercase and atleast  one uppercase character \n")


#Password validation function

def pval():
    while True:
        # password input by the user
        password = input("Enter a password: ")
        #checks the minimum length of the password
        if len(password) < 6:
            print("Password length should be atleast 6 characters")
        #checks the maximum length of the password
        elif len(password) > 16:
            print("Password length should not be morethan 16 characters")
        #checks if the password entered has a number init or not
        elif re.search('[0-9]', password) is None:
            print("Password should have a number")
        #checks if the password entered has a special character init or not
        elif re.search('[$@!*]', password) is None:
            print("Password should have atleast one special character in $@!* letter")
        #checks if the password entered has an uppercase letter or not
        elif re.search('[A-Z]',password) is None:
            print("Password should have atleast one uppercase letter")
        #checks if the password entered has a lowercase letter or not
        elif re.search('[a-z]',password) is None:
            print("Password should have atleast one lowercase letter")
        #if everything is valid it prints the valid statement
        else:
            print("Password entered is valid")
            break

pval()
