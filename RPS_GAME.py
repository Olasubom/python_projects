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
        try:
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
                print("YOU WIN🥳😎")
                
            elif player == computer:
                print("TIE TRY AGAIN😱😱")
            else:
                print("COMPUTER WINS💀🤖")

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
        except ValueError:
             return game()            
    


game()          


# name= "player"

