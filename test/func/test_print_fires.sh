test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run check_basic_functionality python ../../src/print_fires.py --file_name "test_data.csv" --country "Serbia" --country_column 0
assert_exit_code 0
assert_stdout
assert_in_stdout 2006

run add_optional_inputs python ../../src/print_fires.py --file_name "test_data.csv" --country "Serbia" --country_column 0 --result_column 3 --stats "mean"
assert_exit_code 0
assert_stdout

run check_bad_query_index python ../../src/print_fires.py --file_name "test_data.csv" --country "Serbia" --country_column 0 --result_column 32
assert_exit_code 1
assert_stdout

run check_bad_query_index python ../../src/print_fires.py --file_name "test_data.csv" --country "Serbia" --country_column 0 --result_column 0
assert_exit_code 1
assert_stdout

run check_wrong_file_name python ../../src/print_fires.py --file_name "wrong_name.csv" --country "Serbia" --country_column 0 --result_column 3
assert_exit_code 1
assert_stdout

run check_wrong_file_name python ../../src/print_fires.py --file_name "test_data.csv" --country "Serbia" --country_column 0 --result_column 3 --stats "blah"
assert_exit_code 1
assert_stdout
assert_in_stdout "statistical test"