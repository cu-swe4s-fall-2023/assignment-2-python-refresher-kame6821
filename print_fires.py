import my_utils
import argparse
import sys


def main():
    # Allowing function parameters to be called from command line
    parser = argparse.ArgumentParser(prog="print_fires",
                                     description="Print desired info from csv")

    parser.add_argument("--file_name",
                        type=str,
                        help="Name of the file (string)",
                        required=True)

    parser.add_argument("--country_column",
                        type=int,
                        help="Index of col with country names (integer)",
                        required=True)

    parser.add_argument("--country",
                        type=str,
                        help="Name of the country to query (string)",
                        required=True)

    parser.add_argument("--result_column",
                        type=int,
                        help="Index of col with desired info; default = 1",
                        default=1,
                        required=False)

    args = parser.parse_args()

    # Handling common exceptions
    try:
        f = open(args.file_name, 'r')

        # Printing information from desired column in data file
        forest_fires = my_utils.get_column(args.file_name,
                                           args.country_column,
                                           args.country,
                                           args.result_column)
        print(forest_fires)
    except FileNotFoundError:
        print('Could not find ' + args.file_name)
    except PermissionError:
        print('Could not open ' + args.file_name)
    except IndexError:
        print('At least one column index not in chosen file')
    finally:
        print('Data for file name ' + args.file_name)


if __name__ == "__main__":
    main()
