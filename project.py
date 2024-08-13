import sys
import random
import string
from enum import Enum

class RPS(Enum):
    rock = 1
    paper = 2
    scissors = 3

def game():
    while True:
        player_one = input("INPUT A NUMBER :\n1.rock\n2.paper\n3.scissors\n")
        player = int(player_one)
        if player < 1 or player > 3:
            print("YOU HAVE EXCEEDED THE INPUT REQUIRED")
            return game()

        player_two = random.choice([1,2,3])
        computer = int(player_two)
        print("")
        print("YOU CHOOSE " + str(RPS(player)).replace("RPS." , "") + ".")    
        print("COMPUTER CHOOSE " + str(RPS(computer)).replace("RPS." , "") + ".")

        if player == 1 and computer == 3 or player == 3 and computer == 2 or player == 2 and computer == 1:
            print("YOU WIN!!")
            
        elif player == computer:
            print("TIE TRY AGAIN")
        else:
            print("COMPUTER WINS!!")

        while True:
            play_again = str(input("\n Y for yes \n Q for quit\n")).lower()
            if play_again not in ["y" , "q"]:
                print("input is not 'Y' or 'Q'")
                continue
            else:
                break
        if play_again == "y":
            return game()
        else:
            print("THANKS FOR PLAYING😁")
            sys.exit("BYE😭😭")      
    
    


game()                

print("")
print("")


def password_gen():
    previous_password = None
    while True:
        try:
            password_characters = string.ascii_letters + string.digits
            password_len = random.randint(8 ,10)
            current_password = ''.join(random.choices(password_characters , k=password_len))

            if previous_password is not None:
                print(f"Previous password: {previous_password}")
            print(f"New password: {current_password}\n")
            previous_password = current_password

            regenerate_password = input(f"Do you want to regenerate a password y/n\n")
            if regenerate_password.lower() != "y":
                if regenerate_password.lower() != "n":
                    sys.exit("The  required input is 'y'/'n' ")
                else:
                    break      
        except ValueError:
            return("There seem to be an error while regenerating ")

password_gen()

print("")

def calculator():
    try:
        num_1 = float(input("input any number = "))
        num_2 = float(input("input any number = "))


        print("choose any operators")
        print("1. addition (+)")
        print("2. subtraction (-)")
        print("3. multiplication (*)")
        print("4. division (/)")
        print("5. modulus (%)")
        operators = input("input an operator:\n")

        if operators == "1":
                result =  num_1 + num_2
                print(f"{num_1} + {num_2} = {result}")
        elif operators == "2":
                result =  num_1 - num_2
                print(f"{num_1} - {num_2} = {result}")
        elif operators == "3":
                result =  num_1 * num_2
                print(f"{num_1} * {num_2} = {result}")
        elif operators == "4":
                result =  num_1 / num_2
                print(f"{num_1} / {num_2} = {result:.2f}")
        elif operators == "5":
                result =  num_1 % num_2
                print(f"{num_1} % {num_2} = {result}")
        else:
            print("enter a valid operator")
    except  ValueError:
           sys.exit("syntax error")             

calculator()


print("")











