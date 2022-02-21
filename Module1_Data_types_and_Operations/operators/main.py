# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line

# 1
switzerland_most_spoken = 'German'
spain_most_spoken = 'Castilian Spanish'
print(switzerland_most_spoken == spain_most_spoken)

# 2
switzerland_prevalent_religion = 'Roman Catholic'
spain_prevalent_religion = 'Roman Catholic'
print(switzerland_prevalent_religion == spain_prevalent_religion)

# 3
switzerland_capital_name_length = len('Zurich')
spain_capital_name_length = len('Madrid')
print(spain_capital_name_length != switzerland_capital_name_length)

# 4
switzerland_GDP = 4.9
spain_GDP = 4.2
print(switzerland_GDP > spain_GDP)

# 5
switzerland_population_growth = 0.65
spain_population_growth = -0.03
print(switzerland_population_growth and spain_population_growth < 1)

# 6
switzerland_population_count = 8453550
spain_population_count = 47260584
print(switzerland_population_count >
      10000000 or spain_population_count > 10000000)

# 7
switzerland_population_count = 8453550
spain_population_count = 47260584
print(switzerland_population_count > 10000000 or spain_population_count >
      10000000 and switzerland_population_count < 10000000 or spain_population_count < 10000000)
