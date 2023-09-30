#!/bin/bash

set -e # Stop on error
set -u # Raise error if variable is unset

echo # To make outputs easier to read

# Example of functioning inputs
python print_fires.py --file_name "../data/Agrofood_co2_emission.csv" --country "United States of America" --country_column 0 --result_column 3
echo

# Example of input that will raise error in get_column
python print_fires.py --file_name "../data/Agrofood_co2_emission.csv" --country "United States of America" --country_column 0 --result_column 0
echo

# Example of input that will raise error in print_fires
python print_fires.py --file_name "../data/Agrofood_co2_emission.csv" --country "United States of America" --country_column 0 --result_column 31
echo