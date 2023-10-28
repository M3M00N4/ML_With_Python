import pandas as pd 

# Read Data from CSV File
data = pd.read_csv("data_cleaning.csv")
print(data)

# Drop Duplicates
# Drop_duplicates() removes the duplicate rows from the dataframe
data = data.drop_duplicates()

# Drop Extra Columns
# Drop() removes the column provided in () from the dataframe
data = data.drop(columns = "Not_Useful_Column")

# Remove Extra Values
# Strip() removes the value provided in () from both sides of the string 
data["Last_Name"] = data["Last_Name"].str.strip("._/")
print(data)

# Extend Address into Streed, State and Zip Code
data[['Address', 'State', 'Zip_Code']] = data["Address"].str.split(",", expand=True)
print(data)

# Drop State and Zip Code Column
data = data.drop(columns = ["State", "Zip_Code"])
print(data)

# Replace Yes witl Y and No with N for Do_Not_Contact Column
data["Do_Not_Contact"] = data["Do_Not_Contact"].str.replace('Yes','Y')
data["Do_Not_Contact"] = data["Do_Not_Contact"].str.replace('No','N')
print(data)

# Remove All NA Values
data=data.fillna('')
print(data)

# Drop All The Y Values In Do_Not_Contact 
for x in data.index:
    if data.loc[x, "Do_Not_Contact"] == 'Y':
        data.drop(x, inplace=True)
print(data)

# Drop All Where Number is Not Provided
for x in data.index:
    if data.loc[x, "Phone_Number"] == '':
        data.drop(x, inplace=True)
print(data)

data = data.reset_index(drop=True)
print(data)