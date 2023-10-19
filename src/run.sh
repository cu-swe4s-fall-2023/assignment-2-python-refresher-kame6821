#!/bin/bash

set -u # Raise error if variable is unset

echo # To make outputs easier to read

# Run to get populations comparison
python plot_data.py --file_name "../data/Agrofood_co2_emission.csv" --country_list "United States of America" --country_column 0 --result_column_list 1 28 --x_y_labels "Year" "Number of Females" --plot_name "snakemake_outputs/'United States of America'"
echo

# Run to try Mexico
python plot_data.py --file_name "../data/Agrofood_co2_emission.csv" --country_list "Mexico" --country_column 0 --result_column_list 1 28 --x_y_labels "Year" "Number of Females" --plot_name "snakemake_outputs/Mexico.png"
echo

# Example of functioning inputs
python print_fires.py --file_name "../data/Agrofood_co2_emission.csv" --country "United States of America" --country_column 0 --result_column 3
echo

# Example of functioning inputs with optional statistical test
python print_fires.py --file_name "../data/Agrofood_co2_emission.csv" --country "United States of America" --country_column 0 --result_column 3 --stats "mean"
echo

# Example of input that will raise error in get_column
python print_fires.py --file_name "../data/Agrofood_co2_emission.csv" --country "United States of America" --country_column 0 --result_column 0
echo

# Example of input that will raise error in print_fires
python print_fires.py --file_name "../data/Agrofood_co2_emission.csv" --country "United States of America" --country_column 0 --result_column 31
echo

# Example of input that will raise error in print_fires
python print_fires.py --file_name "../data/Agrofood_co2_emission.csv" --country "United States of America" --country_column 0 --result_column 3 --stats "blah"
echo