import sys

"""Library of math functions:
    * get_column -- returns desired information from data file
    * find_mean -- returns mean of an integer array
    * find_median -- returns median of an integer array
    * find_std -- returns standard deviation of an integer array
"""


def get_column(file_name, query_column, query_value,
               result_column=1, stats=None):
    """Searches file for matches in one column and returns data from another

    Parameters
    ----------
    file_name : str
        Name of file (i.e. csv or txt) with delimited rows and columns of data
    query_column: int
        Column index to be searched to match query_value
    query_value: str
        The value to match to finding data on it in other columns
    result_col: int (default = 1)
        Column index with desired info to be returned
    stats: str (default = None)
        Name of desired statistical function to run on output data

    Returns
    -------
    result_column_array
        List of data entries from desired subset
    """
    f = open(file_name, 'r')
    result_column_list = []
    for line in f:
        A = line.rstrip().split(',')
        if A[query_column] == query_value:
            result_column_list.append(A[result_column])

    result_column_list = [int(float(i)) for i in result_column_list]
    if stats == "mean":
        return find_mean(result_column_list)
    if stats == "median":
        return find_median(result_column_list)
    if stats == "std":
        return find_std(result_column_list)
    if stats is None:
        return result_column_list
    else:
        raise ValueError("Selection not an option for a statistical test.",
                         " Please select mean, median, std, or ",
                         "select no input to return desired data array")
        return None


def find_mean(integer_array):
    """Finds the average value of an array of integers

    Parameters
    -------
    integer array: nx1 array
        Every value in the one-dimensional array is an integer

    Returns
    -------
    array_mean
        A single value representing the array's average
    """
    if len(integer_array) <= 0:
        raise ValueError("Length of array must be greater than zero")
    for value in integer_array:
        if "int" == type(value) is False:
            raise TypeError("Value %s in list is not an integer" % value)
            sys.exit(1)
    array_mean = sum(integer_array)/len(integer_array)
    return array_mean


def find_median(integer_array):
    """Finds the median value of an array of integers

    Parameters
    -------
    integer array: nx1 array
        Every value in the one-dimensional array is an integer

    Returns
    -------
    array_median
        A single value representing the array's median
    """
    if len(integer_array) <= 0:
        raise ValueError("Length of array must be greater than zero")
        sys.exit(1)
    for value in integer_array:
        if "int" == type(value) is False:
            raise TypeError("Value %s in list is not an integer" % value)
            sys.exit(1)
    integer_array.sort()
    array_len = len(integer_array)
    # Check if array has an odd or even length
    if array_len % 2 != 0:
        array_median = integer_array[int((array_len)/2)]
    else:
        array_median = (integer_array[int((array_len/2))] +
                        integer_array[int(array_len/2-1)])/2
    return array_median


def find_std(integer_array):
    """Finds the standard deviation of an array of integers

    Parameters
    -------
    integer array: nx1 array
        Every value in the one-dimensional array is an integer

    Returns
    -------
    array_median
        A single value representing the array's standard deviation
    """
    if len(integer_array) <= 0:
        raise ValueError("Length of array must be greater than zero")
        sys.exit(1)
    array_mean = find_mean(integer_array)
    total_numerator = sum((value - array_mean) ** 2 for value in integer_array)
    array_std = (total_numerator/len(integer_array)) ** 0.5
    return array_std
