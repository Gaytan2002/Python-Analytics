import pandas as pd

df = pd.read_csv("/Users/gabrielgaytaniii/Desktop/codes/Projects/Python Workshop/dta.csv")

print("Preview of the Dataset:")
print(df.head())

print("Information about the Dataset:")
print(df.info())

print("Shape of the Dataset:")
print(df.shape)

print("Column names in the Dataset:")
print(df.columns)

print("Missing Values in the Dataset:")
print(df.isnull().sum())

df.rename(columns={
    'Emissions_per_Capita': 'Emissions Per Capital'
}, inplace=True)

print("Updated Column Names:")
print(df.columns)

high_emitters = df[df["Emissions"] > 2000000]
print("Countries with High Emissions:")
print(high_emitters)

sorted_per_capital = df.sort_values(by="Emissions Per Capital", ascending=False)
print("Countries sorted by Emissions Per Capital:")
print(sorted_per_capital)

sorted_emissions = df.sort_values(by="Emissions", ascending=False)
print("Countries sorted by Total Emissions:")
print(sorted_emissions)

avg_emissions_per_capital = df["Emissions Per Capital"].mean()
print(f"Average Emissions Per Capital: {avg_emissions_per_capital}")

total_emissions = df["Emissions"].sum()
print(f"Total Global Emissions: {total_emissions}")


