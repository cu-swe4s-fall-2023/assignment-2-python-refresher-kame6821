#!/bin/bash

set -u # Raise error if variable is unset

echo # To make outputs easier to read

# Run to get populations comparison
python data_analysis.py --file_name "../data/Agrofood_co2_emission.csv" --country_list "China" "Russia" "Nigeria" "United States of America" "Brazil" "Australia" --country_column 0 --result_column_list 1 29 --x_y_labels "Year" "Number of People" --plot_name "Total Population Trend"