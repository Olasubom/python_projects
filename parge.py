import argparse
from passarg import generate_password

if __name__ == "__main__":
    project = argparse.ArgumentParser(
       description= "Provids generated password to user"
    )

    project.add_argument(
        "-l","--length",
      type=int,
      required=True,
      help="the lenght of your password"
    )

    args = project.parse_args()
    password = generate_password(args.length)
    print(f"Password: {password}")