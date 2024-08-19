import string
import random
import sys


def password_gen():
    privious_password = None
    while True:
        try:
            password_char = string.digits + string.ascii_letters
            password_len = random.randint(8,10)
            current_password = ''.join(random.choices(password_char , k=password_len))

            if privious_password is not None:
                print(f"ypur privious password: {privious_password}")
            print(f"your new password:{current_password}") 

            privious_password = current_password

            regenerate_password = input("do you want to regenerate a new password Y/N\n")
                
            if regenerate_password.lower()!= "y":
                if regenerate_password.lower() != "n":
                    sys.exit("input y/n")
                else:
                    break
        except ValueError:
            print("there seem to be an error while regenerating")    

# password_gen()           
        

if __name__== "__main__":
    password_gen()