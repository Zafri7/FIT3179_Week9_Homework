#%%
import pandas as pd

# Load the Malaria and Final_Cleaned_GDP data
malaria_df = pd.read_csv('Malaria.csv')
gdp_df = pd.read_csv('Final_Cleaned_GDP.csv')

# Convert the Population column to numeric, errors='coerce' will replace invalid parsing to NaN
malaria_df['Population'] = pd.to_numeric(malaria_df['Population'], errors='coerce')

# Extract population based on the country from Malaria data
population_df = malaria_df[['Country', 'Population']].drop_duplicates()

# Merge the population data into the Final_Cleaned_GDP data
merged_df = pd.merge(gdp_df, population_df, on='Country', how='left')

# Create a new column for GDP per capita
# Multiply GDP by 1,000,000 (since it's in millions) before dividing by Population
merged_df['GDP_per_Capita'] = (merged_df['GDP'] * 1_000_000) / merged_df['Population'].fillna(0)

# Save the updated DataFrame to a new CSV file
merged_df.to_csv('Final_Cleaned_GDP_with_Per_Capita.csv', index=False)


#%%
import pandas as pd

# Load the 'Final_Merged_With_School_Develop.csv' file
final_merged_df = pd.read_csv('Final_Merged_With_School_Develop.csv')

# Load the 'GDP 2.csv' file
gdp2_df = pd.read_csv('GDP 2.csv')


# List of years to filter (as columns in the DataFrame)
years_to_filter = [str(year) for year in range(2000, 2016)]

# List of unique countries in 'Final_Merged_With_School_Develop.csv'
unique_countries_final_merged = final_merged_df['Country'].unique()

# Filter 'GDP 2.csv' to only include countries that are in 'Final_Merged_With_School_Develop.csv'
gdp2_df_filtered = gdp2_df[gdp2_df['Country'].isin(unique_countries_final_merged)]

# Filter the DataFrame to only include the years 2000 to 2015
gdp2_df_filtered = gdp2_df_filtered[['Country'] + years_to_filter]

# Save this new DataFrame to a CSV file
output_path = 'Filtered_GDP_2000_2015.csv'
gdp2_df_filtered.to_csv(output_path, index=False)


