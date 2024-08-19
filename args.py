from greetings import greetings
import argparse

if __name__ == "__main__":
    argument = argparse.ArgumentParser(
        description="provide a personal greetings to user"
    )

    argument.add_argument(
        "-n","--name",
        metavar="name",
        required=True,
        help="The name of the person to greet"
    )

    argument.add_argument(
        "-l","--lang",
        metavar="language",
        required=True,
        choices=["English","Spanish","French","Yoruba"],
        help="The language of the greeting"    
    
    )

    args = argument.parse_args()
    greetings(args.name ,args.lang)