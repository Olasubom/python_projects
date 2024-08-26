import random
import sys


def gmn(name= "player_choose"):
    print(f"welcome to a chooseing game\n")
    game_count = 0
    player_count = 0

    def game():
        nonlocal player_count
        while True:
            print("guess the number am thinking of.....1, 2, or 3\n")
            computer = random.randint(1 , 3)

            player_choose = int(input())
            if player_choose < 1 or player_choose > 3:
                print(f"{name} the input required is 1 , 2 , 3\n")
                return game()
            print(f"{name} you choose {player_choose}")
            print(f"I was thinking of number {computer}")


            if player_choose == 1 and computer == 3 or player_choose == 3 and computer == 1:
                print("Your winning percentage is: 33.33%")
            elif player_choose == 2 and computer == 1 or player_choose == 1 and computer == 2:
                print("Your winning percentage is: 50.00%") 
            elif player_choose == 2 and computer == 3 or player_choose == 3 and computer == 2:
                print("Your winning percentage is: 50.00%")
            elif player_choose == computer:
                player_count += 1
                print ("Your winning percentage is: 100.00%")

            nonlocal game_count
            game_count += 1 
            print(f"\nGAME COUNT: {game_count}")
            print(f"{name} count: {player_count}")  
        
            print("\nPlay again")
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
                
                if __name__== "__main":
                    sys.exit(f"BYE {name} 😭😭")
                else:
                    return   
    game()    
 

if __name__ == "__main__":
     import argparse
     key = argparse.ArgumentParser(
        description="this is a chooosing game"
    )

     key .add_argument(
        "-n","--name",
        metavar= "name",
        type=str,
        required=True,
        help="the name of the person playing the game"
    )
     
     args = key.parse_args()
     gmn(args.name)
     gmn()


