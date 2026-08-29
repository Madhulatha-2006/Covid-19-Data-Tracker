import pandas as pd
import matplotlib.pyplot as plt
import os

# Load the CSV dataset
file_path = "data/covid_data.csv"

try:
    data = pd.read_csv(file_path)
    print("COVID-19 dataset loaded successfully!")

except FileNotFoundError:
    print("Error: covid_data.csv not found.")
    print("Make sure the data folder contains covid_data.csv.")
    exit()

# Display the dataset
print("\nCOVID-19 Dataset:")
print(data)

# Find top 5 countries
top_5 = data.sort_values(
    by="Total_Cases",
    ascending=False
).head(5)

# Display top 5 countries
print("\nTop 5 Countries by Total COVID-19 Cases:")
print("-------------------------------------------")
print(top_5.to_string(index=False))

# Create output folder
os.makedirs("output", exist_ok=True)

# Save top 5 results
top_5.to_csv(
    "output/top_5_countries.csv",
    index=False
)

# Create bar chart
plt.figure(figsize=(10, 6))

plt.bar(
    top_5["Country"],
    top_5["Total_Cases"]
)

plt.title("Top 5 Countries by Total COVID-19 Cases")
plt.xlabel("Country")
plt.ylabel("Total Cases")

plt.xticks(rotation=45)

plt.tight_layout()

# Save chart
plt.savefig("output/top_5_covid_cases.png")

# Display chart
plt.show()

print("\nTop 5 results saved to output/top_5_countries.csv")
print("Bar chart saved to output/top_5_covid_cases.png")