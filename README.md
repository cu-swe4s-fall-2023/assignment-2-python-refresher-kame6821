# About the Agriculture Data Finder:

This software searches an input file by country and returns desired data for that country across a range of years. 

## Results from basic country data analysis:
The data file is provided here and the user can download it to test reproducibility of results and perform additional analysis: https://drive.google.com/file/d/1Wytf3ryf9EtOwaloms8HEzLG0yjtRqxr/view?usp=drive_link. Initial findings are described below

### Initial findings
Our goal was to assess the agriculture data to explore male population trends over the years in the two most populous countries from each continent.

#### Results: (Coming soon!)


#### Methods: 


## How to use this software:

Clone this repository to your machine. Navigate to the src folder from terminal. Edit the run.sh file to achieve the desired outputs with the provided files (described in "Methods" of the "Initial Findings" section above) using Python. Run the following from the terminal, and outputs will be created.
```
bash run.sh
```

To compare male populations in different countries, you can also use the snakefile provided in the src directory. Add the names of countries you want to visualize in the list at the top of the snakefile, save the file, then run "snakemake --cores N" (without the quotes) from the terminal within the src directory, replacing N with the number of cores to be used. 

Note that print_fires.py is auxiliary code that can be used to print desired data 

## Installation:

Clone the github repository and ensure python is installed on your local machine.

To run unit tests, cd into test/unit directory and run the following in the terminal: python -m unittest test_my_utils.py

To run functional tests, cd into test/func directory and run the following in the terminal: bash test_print_fires.sh

# Information on releases:

### Release V1.0 (Assignment 2) Python Refresher:
Wrote updated get_column function with query functionality. Edited print_fires.py to print info on US forest fires. Added a run.sh file.

### Release V2.0 (Assignment 3) Best Practices:
Updated print_fires.py to work with command line arguments and include a main_function. Updated get_columns function in my_utils to convert output to integer. Updated run.sh to include a functioning example and two examples that create errors. Documentation updated in all files.

#### Release V2.1:
Added correct folder structure, exit codes in print_fires, and .gitignore file.

### Release V3.0 (Assignment 4):
Created test_my_utils.py unit tests and test_print_fires.sh functional tests. Added new statistical test functions in my_utils.py and add the option to include those functions as inputs in print_fires.py. Updated .gitignore file accordingly.

#### Release V3.1:
Included instructions on how to run tests in readme, updated test_my_utils and my_utils to fix a mistake, moved data files to separate data folder and corrected relevant paths.

### Release V4.0 (Assignment 5):
Added an environment file. Added github workflows to run auto testing on every push and pull request (for style checks, unit tests, and funcational tests). Cleaned up folder structure.

### Release V5.0 (Assignment 6):
Provided example results in readme about the data file used. Added a snakemake pipeline to reproduce results discussed in this project's overview (above). Added unit and functional tests for new code. 