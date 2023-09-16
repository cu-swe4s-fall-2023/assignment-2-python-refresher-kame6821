# About the Agriculture Data Finder:

This software searches an input file by country and returns desired data for that country across a range of years. 

## How to use this software:

Run the following in command line, changing out the file name, country, and column indexes as needed:
'''
python print_fires.py --file_name "Agrofood_co2_emission.csv" --country "United States of America" --country_column 0 --result_column 3
'''

## Installation:

Clone the github repository and ensure python is installed on your local machine.

# Information on releases:

### Release V1.0 (Assignment 2) Python Refresher:
Wrote updated get_column function with query functionality. Edited print_fires.py to print info on US forest fires. Added a run.sh file.

### Release V2.0 (Assignment 3) Best Practices:
Updated print_fires.py to work with command line arguments and include a main_function. Updated get_columns function in my_utils to convert output to integer. Updated run.sh to include a functioning example and two examples that create errors. Documentation updated in all files.

