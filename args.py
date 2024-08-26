from greetings import greetings
import argparse

if __name__ == "__main__":

    project = argparse.ArgumentParser(
        description="greetings in any language"
    )
    project.add_argument(
        "-n","--name",
        metavar="name",
        required=True,
        help="the name of the person to greet"
    )
    project.add_argument(
        "-l","--lang",
        metavar= "language",
        required=True,
        choices=["English","Spnish","French","Yoruba"],
        help="The language preferd"
    )
    args = project.parse_args()
    greetings(args.name ,args.lang)