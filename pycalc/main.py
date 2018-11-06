#!/usr/bin/python
from pycalc import Calc
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Pure-python command-line calculator.")
    parser.add_argument("EXPRESSION", help="expression string to evaluate", type=str)
    parser.add_argument("-m", "--use-modules", metavar="MODULE", nargs="+", help="additional modules to use")
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    print(Calc.calculate(args.EXPRESSION))


if __name__ == "__main__":
    main()
