import pandas as pd
import matplotlib.pyplot as plt

# Load data from a CSV file into a pandas DataFrame
data = pd.read_csv("pandas.csv")

# Display the first few rows of the dataset
print("First 5 rows of the dataset:")
print(data.head())

# Display the last few rows of the dataset
print("Last 5 rows of the dataset:")
print(data.tail())

# Display information about the dataset, including data types and null values
print("Dataset information:")
print(data.info())

# Generate summary statistics of the numerical columns in the dataset
print("Summary statistics of the dataset:")
print(data.describe())

# Extract and display the "Name" column
print("Names in the dataset:")
print(data["Name"])

# Display the first name in the "Name" column
print("First name in the dataset:")
print(data["Name"][0])

# Calculate and display the minimum, mean, and maximum age
print("Minimum age in the dataset:")
print(data["Age"].min())
print("Mean age in the dataset:")
print(data["Age"].mean())
print("Maximum age in the dataset:")
print(data["Age"].max())

# Generate summary statistics of the "Age" column
print("Summary statistics of the Age column:")
print(data["Age"].describe())

# Filter and display rows where age is greater than 30
print("People aged over 30:")
print(data[data["Age"] > 30])

# Extract names of people aged over 30
print("Names of people aged over 30:")
print(data[data["Age"] > 30]["Name"])

# Count the number of names where age is greater than 30
print("Count of names where age is greater than 30:")
print(data[data["Age"] > 30]["Name"].count())

# Create a histogram to visualize the age distribution
plt.hist(data["Age"])
plt.xlabel("Age")
plt.ylabel("Number of People")
plt.title("Age Distribution")
plt.show()
