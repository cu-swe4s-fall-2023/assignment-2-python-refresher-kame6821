"""Library of math functions:
    * get_column -- returns desired information from data file
"""


def get_column(file_name, query_column, query_value, result_column=1):
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

    Returns
    -------
    result_column_array
        List of data entries from desired subset
    """
    f = open(file_name, 'r')
    result_column_array = []
    for line in f:
        A = line.rstrip().split(',')
        if A[query_column] == query_value:
            result_column_array.append(A[result_column])

    try:
        result_column_array = [int(float(i)) for i in result_column_array]
    except ValueError:
        print('Could not convert result_column values to integer')
    finally:
        return result_column_array
