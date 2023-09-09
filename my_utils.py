def get_column(file_name, query_column, query_value, result_column):
    f = open(file_name, 'r')
    result_column_array = []
    for l in f:
        A = l.rstrip().split(',')
        if A[query_column] == query_value:
            print(A[query_column])
            result_column_array.append(A[result_column])
    return result_column_array
