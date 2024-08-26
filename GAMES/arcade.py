import sys
from GMN import gmn
from RPS_GAME import play_game


def arcade(name="player"):
    welcome = False
    print("\nwelcome to the Arcade 🎰")
    while True:
        if welcome == True:
            print(f"\nwelcome back to the Arcade menu 🎰 {name}")
       
        print("current games......\n") 

        print(f"1 = Rock Paper Scissors")
        print(f"2 = Guess My Number")
        print(f"\npress \"x\" to exit the Arcade \n")
        input_v = input().lower()

        if input_v not in ["1" , "2" ,"x"]:
            print(f"invalid input")
            continue

        welcome = True

        if input_v == "1":
            start_RPS = play_game(name)
            start_RPS()
        elif input_v == "2":
            gmn(name)
        else:
            print(f"Thanks for playing {name}")
            sys.exit()



if __name__ == "__main__":
     import argparse
     key = argparse.ArgumentParser(
        description="this is a arcade game center"
    )

     key .add_argument(
        "-n","--name",
        metavar= "name",
        type=str,
        required=True,
        help="the name of the person playing the arcade"
     )


     args = key.parse_args()
     start_acade = arcade(args.name)
     start_acade()
