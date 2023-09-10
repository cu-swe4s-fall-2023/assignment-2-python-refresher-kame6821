from my_utils import get_column

country='United States of America'
country_column = 0
forest_fires_column = 3
file_name = 'Agrofood_co2_emission.csv'
forest_fires = get_column(file_name, country_column, country, result_column=forest_fires_column)
print(forest_fires)
