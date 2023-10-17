import my_utils
import argparse
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def main():
    # Allowing function parameters to be called from command line
    parser = argparse.ArgumentParser(prog="Agriculture Analysis",
                                     description="Create desired data plots")

    parser.add_argument("--file_name",
                        type=str,
                        help="Name of the file (string)",
                        required=True)

    parser.add_argument("--country_column",
                        type=int,
                        help="Index of col with country names (integer)",
                        required=True)

    parser.add_argument("--country_list",
                        nargs="+", type=str,
                        help="Individual country names (each a str) to query; " + 
                        "format: 'Country name 1' 'Country name 2'",
                        required=True)

    parser.add_argument("--result_column_list",
                        nargs='+', type=int,
                        help="Individual col indices with desired info; max 2 indices" ,
                        required=True)
    
    parser.add_argument("--x_y_labels",
                        nargs="+", type=str,
                        help="x and y label for plot (respectively)",
                        required=True)

    parser.add_argument("--stats",
                        type=str,
                        help="String with desired statistical test name; " +
                        "Options are limited to mean, median, or std; " +
                        "default = None",
                        default=None,
                        required=False)
    
    parser.add_argument("--plot_name",
                        type=str,
                        help="Provide name for plot to output; default = 'MyPlot1'",
                        default="MyPlot1",
                        required=False)
   

    args = parser.parse_args()

    # Handling common exceptions
    try:
        for country in args.country_list:
            x_y_country_results = []
            for desired_col_index in args.result_column_list:
                one_axis_result = my_utils.get_column(args.file_name,
                                                      args.country_column,
                                                      country,
                                                      desired_col_index,
                                                      args.stats)
                x_y_country_results.append(one_axis_result)
            plt.plot(x_y_country_results[0], x_y_country_results[1],label=country)
        
        plt.legend(loc="best")
        plt.xlabel(args.x_y_labels[0])
        plt.ylabel(args.x_y_labels[1])
        plt.title(args.plot_name)
        plt.savefig(args.plot_name,bbox_inches='tight')    
        
    except ValueError:
        print('Output array from get_column cannot be empty and/or \n',
              'could not convert result_column values to integer and/or \n',
              'entered unavailable option for statistical test')
        sys.exit(1)
    except TypeError:
        print('Output array from get_column must only contain integers')
        sys.exit(1)
    except FileNotFoundError:
        print('Could not find ' + args.file_name)
        sys.exit(1)
    except PermissionError:
        print('Could not open ' + args.file_name)
        sys.exit(1)
    except IndexError:
        print('At least one column index not in chosen file')
        sys.exit(1)
    finally:
        print('Data for file name ' + args.file_name)


if __name__ == "__main__":
    main()
