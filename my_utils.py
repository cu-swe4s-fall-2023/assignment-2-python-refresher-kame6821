def get_column(file_name, query_column, query_value, result_column=1):
    f = open(file_name, 'r')
    result_column_array = []
    for l in f:
        A = l.rstrip().split(',')
        if A[query_column] == query_value:
            result_column_array.append(A[result_column])
    return result_column_array
