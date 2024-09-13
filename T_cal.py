from progs import calculator
from args import argparse


if __name__ == ("__main__"):
    project = argparse.ArgumentParser(
        description=" A command line calculator that takes two numbers and operation as an argument"

    )

    project.add_argument(
        "-a", "--number1",
        metavar="number1",
        type=int,
        required=True,
        help="enter a number"

    )
    project.add_argument(
        "-b", "--number2",
        metavar="number2",
        type=int,
        required=True,
        help="enter a number"

    )
    project.add_argument(
        "-o", "--operation",
        metavar="operation",
        type=int,
        required=True,
        choices=[1, 2, 3, 4, 5],
        help="Choose an operation: 1 = Addition, 2 = Subtraction, 3 = Multiplication, 4 = Division, 5 = Modulus"
    )

    args = project.parse_args()
    calculator(args.number1 , args.number2 , args.operation)