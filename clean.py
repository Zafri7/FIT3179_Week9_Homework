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
