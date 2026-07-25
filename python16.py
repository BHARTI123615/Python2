# command_line_demo.py
import sys
import argparse

# --- Part 1: Using sys.argv ---
# Example: python command_line_demo.py add 4 6
if len(sys.argv) > 1:
    operation = sys.argv[1]
    if operation in ["add", "sub", "mul", "div"] and len(sys.argv) == 4:
        a = int(sys.argv[2])
        b = int(sys.argv[3])
        if operation == "add":
            print(f"Sum = {a + b}")
        elif operation == "sub":
            print(f"Difference = {a - b}")
        elif operation == "mul":
            print(f"Product = {a * b}")
        elif operation == "div":
            print(f"Quotient = {a / b if b != 0 else 'Error: divide by zero'}")

# --- Part 2: Using argparse ---
# Example: python command_line_demo.py --op add --x 10 --y 20
parser = argparse.ArgumentParser(description="Mini calculator using argparse")
parser.add_argument("--op", choices=["add", "sub", "mul", "div"], help="Operation")
parser.add_argument("--x", type=int, help="First number")
parser.add_argument("--y", type=int, help="Second number")

args = parser.parse_args()

if args.op and args.x is not None and args.y is not None:
    if args.op == "add":
        print(f"Sum = {args.x + args.y}")
    elif args.op == "sub":
        print(f"Difference = {args.x - args.y}")
    elif args.op == "mul":
        print(f"Product = {args.x * args.y}")
    elif args.op == "div":
        print(f"Quotient = {args.x / args.y if args.y != 0 else 'Error: divide by zero'}")
