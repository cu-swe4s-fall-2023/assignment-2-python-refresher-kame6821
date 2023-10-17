#!/bin/bash

set -u # Raise error if variable is unset

echo # To make outputs easier to read

# Run to get populations comparison
python plot_data.py --file_name "../data/Agrofood_co2_emission.csv" --country_list United States of America --country_column 0 --result_column_list 1 28 --x_y_labels "Year" "Number of Males" --plot_name "Male Population Trend"