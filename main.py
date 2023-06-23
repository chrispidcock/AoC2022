import argparse

parser = argparse.ArgumentParser(description="Runs AoC scripts")

parser.add_argument(
    "-d",
    "--day",
    type=int,
    default=1,
    help="display detailed directory content",
    required=True
)

args = parser.parse_args()

print(args)

if args.day == 1:
    from src import day1
if args.day == 2:
    from src import day2
