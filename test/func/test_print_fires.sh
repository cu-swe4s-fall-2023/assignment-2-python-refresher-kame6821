test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run check_basic_functionality_plot python ../../src/plot_data.py --file_name "../../data/func_test_data.csv" --country "France" --country_column 0 --result_column 1 29 --x_y_labels "Year" "Total Emissions" --plot_name "check_basic_functionality_plot.png"
assert_exit_code 0 
assert_no_stdout

run check_country_name_with_spaces python ../../src/plot_data.py --file_name "../../data/func_test_data.csv" --country "San Marino" --country_column 0 --result_column_list 1 12 --x_y_labels "Year" "Food Retail" --plot_name "check_country_name_with_spaces.png"
assert_exit_code 0
assert_no_stdout

run multiple_countries python ../../src/plot_data.py --file_name "../../data/func_test_data.csv" --country "Serbia" "Spain" --country_column 0 --result_column_list 1 29 --x_y_labels "Year" "Total Emissions" --plot_name "multiple_countries.png"
assert_exit_code 0
assert_no_stdout

run different_result_columns python ../../src/plot_data.py --file_name "../../data/func_test_data.csv" --country "Serbia" "Spain" --country_column 0 --result_column_list 25 26 --x_y_labels "Rural Population" "Urban Population" --plot_name "different_result_columns.png"
assert_exit_code 0
assert_no_stdout

run check_bad_query_index python ../../src/plot_data.py --file_name "../../data/func_test_data.csv" --country "Serbia" "Spain" --country_column 0 --result_column_list 0 --x_y_labels "Rural Population" "Urban Population" --plot_name "check_bad_query_index.png"
assert_exit_code 1
assert_no_stdout

run check_wrong_file_name python ../../src/plot_data.py --file_name "../../data/func_wrong_name.csv" --country "Serbia" --country_column 0 --result_column_list 1 29 --x_y_labels "Year" "Total Emissions" --plot_name "check_wrong_file_name.png"
assert_exit_code 1
assert_no_stdout

run check_test_file python ../../src/plot_data.py --file_name "../../data/func_test_data.csv" --country "Serbia" --country_column 0 --result_column_list 1 29 --x_y_labels "Year" "Total Emissions" --plot_name "check_test_file.png"
assert_exit_code 0
assert_no_stdout

run check_data_with_blanks python ../../src/plot_data.py --file_name "../../data/func_test_data.csv" --country "San Marino" --country_column 0 --result_column_list 1 3 --x_y_labels "Year" "Forest Fires" --plot_name "check_data_with_blanks.png"
assert_exit_code 0
assert_no_stdout

#####

run check_basic_functionality python ../../src/print_fires.py --file_name "../../data/func_test_data.csv" --country "Serbia" --country_column 0
assert_exit_code 0
assert_stdout
assert_in_stdout 2015

run add_optional_inputs python ../../src/print_fires.py --file_name "../../data/func_test_data.csv" --country "Serbia" --country_column 0 --result_column 3 --stats "mean"
assert_exit_code 0
assert_stdout

run check_bad_query_index python ../../src/print_fires.py --file_name "../../data/func_test_data.csv" --country "Serbia" --country_column 0 --result_column 32
assert_exit_code 1
assert_stdout

run check_bad_query_index python ../../src/print_fires.py --file_name "../../data/func_test_data.csv" --country "Serbia" --country_column 0 --result_column 0
assert_exit_code 1
assert_stdout

run check_wrong_file_name python ../../src/print_fires.py --file_name "../../data/func_wrong_name.csv" --country "Serbia" --country_column 0 --result_column 3
assert_exit_code 1
assert_stdout

run check_test_file python ../../src/print_fires.py --file_name "../../data/func_test_data.csv" --country "Serbia" --country_column 0 --result_column 3 --stats "blah"
assert_exit_code 1
assert_stdout
assert_in_stdout "statistical test"