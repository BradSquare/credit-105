import numpy as np
import pandas as pd
from scipy import stats

credit = pd.read_csv("credit.csv")
# credit.info()

#percentage of missing values for each column
missing = credit.apply(lambda x: x.isna().sum()/1000)
print(missing)

#check if ID are all unique values
id = credit["ID"].unique()
print(len(id))

#find rows that are missing values for checking account
checking_account_missing = pd.isnull(credit["Checking_Account"])
missing_ca = credit[checking_account_missing]
print(missing_ca)

#find rows that are missing values for dependents
dependents_missing = pd.isnull(credit["Dependents"])
missing_d = credit[dependents_missing]
print(missing_d)

#fill in empty rows for checking account
credit["Checking_Account"].fillna(4, inplace=True)

#fill in empty rows for dependents
credit["Dependents"].fillna(0, inplace=True)

#percentage of missing values for each column; check if there are still missing values
missing = credit.apply(lambda x: x.isna().sum()/1000)
print(missing)

#check for outliers
print(credit[(np.abs(stats.zscore(credit)) < 3).all(axis=1)])

#checking for invalid values 
'''
#Evaluating Invalid Data (e.g. out of the range) from Personal_Status, Guarantors, Residence_Length and Assets

# Find invalid values (less than 1 or greater than 4) for Personal_Status
invalid_values = df[(df["Personal_Status"] <= 0) | (df["Personal_Status"] > 4)]

# Print results
if not invalid_values.empty:
    print("Invalid Personal_Status values found:")
    print(invalid_values)
else:
    print("All Personal_Status values are valid.")

# Find invalid values (less than 1 or greater than 3) for Guarantors
invalid_values = df[(df["Guarantors"] < 1) | (df["Guarantors"] > 3)]

# Print results
if not invalid_values.empty:
    print("Invalid Guarantors values found:")
    print(invalid_values)
else:
    print("All Guarantors values are valid.")


# Find invalid values (less than 1 or greater than 4) for Residence_Length
invalid_values = df[(df["Residence_Length"] < 1) | (df["Residence_Length"] > 4)]

# Print results
if not invalid_values.empty:
    print("Invalid Residence_Length values found:")
    print(invalid_values)
    
    # Calculate the mode of Residence_Length (excluding invalid values)
    valid_residence = df[(df["Residence_Length"] >= 1) & (df["Residence_Length"] <= 4)]["Residence_Length"]
    residence_mode = valid_residence.mode()[0]  # mode() returns a Series, so we get the first value

    # Replace invalid values with the mode
    df.loc[(df["Residence_Length"] < 1) | (df["Residence_Length"] > 4), "Residence_Length"] = residence_mode

# Re-evaluate Residence_Length for any Invalid values
invalid_values = df[(df['Residence_Length'] < 1) | (df['Residence_Length'] > 4)]

# Print results
if not invalid_values.empty:
    print("Invalid Residence_Length values found:")
    print(invalid_values)
else:
    print("All Residence_Length values are valid.")

# Find invalid values (less than 1 or greater than 4) for Assets
df['Assets'] = pd.to_numeric(df['Assets'])
invalid_values = df[(df["Assets"] < 1) | (df["Assets"] > 4)]

# Print results
if not invalid_values.empty:
    print("Invalid Assets values found:")
    print(invalid_values)
else:
    print("All Assets values are valid.")
'''