import sys
import random
import string
from enum import Enum

def play_game(name= "player"):
    game_count = 0
    player_wins = 0
    computer_wins = 0

    def game():
        nonlocal name
        nonlocal player_wins
        nonlocal computer_wins
        class RPS(Enum):
            rock = 1
            paper = 2
            scissors = 3
        while True:
            try:
                player_one = input(f"\n{name} INPUT A NUMBER :\n\n1.rock\n2.paper\n3.scissors\n")
                player = int(player_one)
                if player < 1 or player > 3:
                    print(f"{name} YOU HAVE EXCEEDED THE INPUT REQUIRED")
                    return game()

                player_two = random.choice([1,2,3])
                computer = int(player_two)
                print("")
                print(f"{name} CHOOSE {str(RPS(player)).replace("RPS." , "")}.")    
                print(f"COMPUTER CHOOSE {str(RPS(computer)).replace("RPS." , "")}.")

                def decide_winner(player , computer):
                    nonlocal player_wins
                    nonlocal computer_wins
                    if player == 1 and computer == 3 or player == 3 and computer == 2 or player == 2 and computer == 1:
                        player_wins += 1
                        print(f"{name} WIN🥳😎")
                        
                    elif player == computer:
                        print("TIE TRY AGAIN😱😱")
                    else:
                        computer_wins += 1
                        print("COMPUTER WINS💀🤖")
                game_result = decide_winner(player ,computer)

                nonlocal game_count
                game_count += 1
                print(f"\nGAME COUNT: {game_count}")
                print(f"{name} COUNT: {player_wins}")
                print(F"COMPUTER COUNT: {computer_wins}\n")

                while True:
                    play_again = str(input("\n Y for yes \n Q for quit\n\n")).lower()
                    if play_again not in ["y" , "q"]:
                        print("input is not 'Y' or 'Q'")
                        continue
                    else:
                        break
                if play_again == "y":
                    return game()
                else:
                    print("\nTHANKS FOR PLAYING😁")
                    if __name__ == "__main__":
                        sys.exit(f"BYE {name}😭😭") 
                    else:
                        return        
            except ValueError:
                print("input 1 , 2 , 3.\n")
                return game()
    return game



if __name__ == "__main__":
    import argparse
    project = argparse.ArgumentParser(
        description="this is an RPS game"
    )

    project.add_argument(
        "-n","--name",
        metavar= "name",
        type=str,
        required=True,
        help="the name of the person playing the game"
    )

    args= project.parse_args()
    start_RPS = play_game(args.name)
    start_RPS()

         


# name= "player"

