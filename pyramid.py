"""Print a pyramid to the terminal
A pyramid of height 3 would look like:
--=--
-===-
=====
"""
from argparse import ArgumentParser, RawDescriptionHelpFormatter


def print_pyramid(rows):

    """Print a pyramid of a given height
    :param int rows: total height
    """

    # loop thru the number of rows in a pyramid
    for i in range(0, rows):
        for j in range(0, (rows - 1) - i):
            # print the - so that we can print the = in the middle
            print("-", end="")
        for j in range(0, 2 * i + 1):
            # print the pyramid shape objects
            print("=", end="")
        for j in range(0, (rows - 1) - i):
            # print the space to place them in middle
            print("-", end="")

        print("")

    # raise NotImplementedError("Called with rows={}".format(rows))


if __name__ == "__main__":

    parser = ArgumentParser(
        description=__doc__, formatter_class=RawDescriptionHelpFormatter
    )

    parser.add_argument("-r", "--rows", default=10, type=int, help="Number of rows")

    args = parser.parse_args()

    print_pyramid(args.rows)
