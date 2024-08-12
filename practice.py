import random
import sys
import string
from enum import Enum

class RPS(Enum):
    rock = 1
    paper = 2
    scissors = 3    
    
# line_one = "***************"
# line_two = "*             *"
# line_3 =  "====welcome====="
# print(line_one)
# print(line_two)
# print(line_3)
# print(line_two)
# print(line_one)    



# player_one  = input("Input a number\n1 rock:\n2 paper:\n3 scissors:\n\n ")
# try:
#     player = int(player_one)

#     if player < 1 or player > 3:
#          print("you have exceed the number")
#          sys.exit(1)
# except ValueError:
#    sys.exit("enter a number")

# player_two = random.choice([1,2,3])
# computer = int(player_two)

# print("")
# print("YOU CHOOSE " + str(RPS(player)).replace("RPS." ,"") + ".")
# print("COMPUTER CHOOSE " + str(RPS(computer)).replace("RPS." , "") + ".")

# if player == 1 and computer == 3 or  player == 3 and computer == 2 or player == 2  and computer == 1:
#     print("YOU WIN!!!")
# elif player ==  computer:
#     print("IT A TIE")
# else:
#     print("COMPUTER WINS")

# print("")

# def calculator():
#     number_one = int(input("input any number: "))
#     number_two = int(input("input ant number: "))
#     print("")
#     print("choose an operator")
#     print("1. addition (+)")
#     print  ("2. subtractiobn(-)")
#     print  ("3. multiplication(*)")
#     print  ("4. division(/)")
#     print("")
#     operator =input("Enter the operator you need = ")

#     if operator == "1":
#         result = number_one + number_two
#         print(f" {number_one} + {number_two} = {result} ")
#     elif operator == "2":
#         result = number_one - number_two
#         print(f" {number_one} - {number_two} = {result}" )
#     elif operator == "3":
#         result = number_one * number_two 
#         print(f" {number_one} * {number_two} = {result}")
#     elif operator == "4":
#         result = number_one / number_two
#         print(f" {number_one} / {number_two} = {result}")
#     else:
#         print("choose a valid  operator!!")

# calculator()
    
game_count = +1
def main():
    while True:
        player_one = input("enter a number\n1.ROCK:\n2.PAPER:\n3.scissors:\n\n")
        try:
            player = int(player_one)
            if player < 1 | player > 3:
                sys.exit("choose 1,2,3.")
                continue
        except ValueError:
            sys.exit("input a number")

        player_two = random.choice([1,2,3])
        computer = int(player_two)

        print("you choose "  + str(RPS(player)).replace("RPS." , "") + ".")
        print("computer choose "  + str(RPS(computer)).replace("RPS." , "") + ".")

        if player ==  1 and computer == 3 | player == 3 and computer == 2 or player == 2 and computer == 1:
            print("YOU WIN!!!")
            break    
        elif player == computer:
            print("TIE TRY AGAIN")
            
        else:
            print("COMPUTER WINS!!!")
            break

main()


# def password_gen():
#     privious_password =  None
#     while True:
#          password_characters = string.ascii_letters + string.digits
#          password_len = random.randint(8, 10)
#          current_password = ''.join(random.choices(password_characters ,  k= password_len))

#          if privious_password is not None:
#               print(f"privious generated password: {privious_password}") 
#          print(f"New generated password: {current_password}")

#          privious_password = current_password

#          Regenerate_password = input("Do you want to regenerate another password? ('y/n')\n")
#          if Regenerate_password != "y":
#               if Regenerate_password != "n":
#                    sys.exit("THE REQUIRED INPUT IS 'y/n'")
#               else:
#                    break 
                   
              
# password_gen()         

