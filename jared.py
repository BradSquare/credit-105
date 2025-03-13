import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv("credit.csv")
# credit.info()

#percentage of missing values for each column
missing = df.apply(lambda x: x.isna().sum()/1000)
#print(missing)

#check if ID are all unique values
id = df["ID"].unique()
#print(len(id))

#find rows that are missing values for checking account
checking_account_missing = pd.isnull(df["Checking_Account"])
missing_ca = df[checking_account_missing]
#print(missing_ca)

#find rows that are missing values for dependents
dependents_missing = pd.isnull(df["Dependents"])
missing_d = df[dependents_missing]
#print(missing_d)

#fill in empty rows for checking account
df["Checking_Account"].fillna(4, inplace=True)

#fill in empty rows for dependents
df["Dependents"].fillna(0, inplace=True)

#percentage of missing values for each column; check if there are still missing values
missing = df.apply(lambda x: x.isna().sum()/1000)
#print(missing)

#check for outliers
print(df[(np.abs(stats.zscore(df)) < 3).all(axis=1)])

#checking for invalid values 

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


#plot for Personal_Status
print(f"Mode: {df['Personal_Status'].mode().iloc[0]}")

df["Personal_Status"] = df["Personal_Status"].astype(str)
data = df["Personal_Status"].value_counts(normalize=True)
data = data.sort_index(key=lambda x: x.astype(int))
xs = data.index
ys = data
plt.figure(figsize=(8,5))
bars = plt.bar(xs, ys, color='skyblue')
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2.,  
        height + 0.01,                     
        f'{height:.1%}',                   
        ha='center',                       
        va='bottom',                        # vertical alignment
        fontsize=9                          # smaller font size
    )
plt.title("Number of Applicants by Personal Status", fontsize=15)
plt.ylabel("Number of Applicants", fontsize=12)
plt.xlabel("Personal Status", fontsize=12)
plt.show()

#plot for Guarantors
print(f"Mode: {df['Guarantors'].mode().iloc[0]}")

df["Guarantors"] = df["Guarantors"].astype(str)
data = df["Guarantors"].value_counts(normalize=True)
data = data.sort_index(key=lambda x: x.astype(int))
xs = data.index
ys = data
plt.figure(figsize=(8,5))
bars = plt.bar(xs, ys, color='skyblue')
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2.,  
        height + 0.01,                     
        f'{height:.1%}',                   
        ha='center',                       
        va='bottom',                      
        fontsize=9                      
    )
plt.title("Number of Applicants by Guarantors", fontsize=15)
plt.ylabel("Number of Applicants", fontsize=12)
plt.xlabel("Guarantors", fontsize=12)
plt.show()

#plot for Residence_Length
print(f"Mode: {df['Residence_Length'].mode().iloc[0]}")

df["Residence_Length"] = df["Residence_Length"].astype(str)
data = df["Residence_Length"].value_counts(normalize=True)
data = data.sort_index(key=lambda x: x.astype(int))
xs = data.index
ys = data
plt.figure(figsize=(8,5))
bars = plt.bar(xs, ys, color='skyblue')
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2.,  
        height + 0.01,                     
        f'{height:.1%}',                   
        ha='center',                       
        va='bottom',                      
        fontsize=9                      
    )
plt.title("Number of Applicants by Residence_Length", fontsize=15)
plt.ylabel("Number of Applicants", fontsize=12)
plt.xlabel("Residence_Length", fontsize=12)
plt.show()

#plot for Assets
print(f"Mode: {df['Assets'].mode().iloc[0]}")

df["Assets"] = df["Assets"].astype(str)
data = df["Assets"].value_counts(normalize=True)
data = data.sort_index(key=lambda x: x.astype(int))
xs = data.index
ys = data
plt.figure(figsize=(8,5))
bars = plt.bar(xs, ys, color='skyblue')
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2.,  
        height + 0.01,                     
        f'{height:.1%}',                   
        ha='center',                       
        va='bottom',                      
        fontsize=9                      
    )
plt.title("Number of Applicants by Assets", fontsize=15)
plt.ylabel("Number of Applicants", fontsize=12)
plt.xlabel("Assets", fontsize=12)
plt.show()

#plot for Personal_Status and approval rate
df["Personal_Status"] = df["Personal_Status"].astype(str)

data = df.groupby("Personal_Status")["Approval"].mean()

xs = data.index 
ys = data

plt.figure(figsize=(8, 5))
bars = plt.bar(xs, ys, color='skyblue')
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2.,  
        height + 0.01,                     
        f'{height:.1%}',                   
        ha='center',                       
        va='bottom',                      
        fontsize=9                      
    )
plt.title("Approval Rate by Personal_Status", fontsize=15)
plt.xlabel("Personal_Status", fontsize=12)
plt.ylabel("Approval Rate", fontsize=12)

plt.ylim(0, 1)

plt.show()

#plot for Guarantors and approval rate
df["Guarantors"] = df["Guarantors"].astype(str)

data = df.groupby("Guarantors")["Approval"].mean()

xs = data.index 
ys = data

plt.figure(figsize=(8, 5))
bars = plt.bar(xs, ys, color='skyblue')
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2.,  
        height + 0.01,                     
        f'{height:.1%}',                   
        ha='center',                       
        va='bottom',                      
        fontsize=9                      
    )
plt.title("Approval Rate by Guarantors", fontsize=15)
plt.xlabel("Guarantors", fontsize=12)
plt.ylabel("Approval Rate", fontsize=12)

plt.ylim(0, 1)

plt.show()

#plot for Residence_Length and approval rate
df["Residence_Length"] = df["Residence_Length"].astype(str)

data = df.groupby("Residence_Length")["Approval"].mean()

xs = data.index 
ys = data

plt.figure(figsize=(8, 5))
bars = plt.bar(xs, ys, color='skyblue')
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2.,  
        height + 0.01,                     
        f'{height:.1%}',                   
        ha='center',                       
        va='bottom',                      
        fontsize=9                      
    )
plt.title("Approval Rate by Residence_Length", fontsize=15)
plt.xlabel("Residence_Length", fontsize=12)
plt.ylabel("Approval Rate", fontsize=12)

plt.ylim(0, 1)

plt.show()

#plot for Assets and approval rate
df["Assets"] = df["Assets"].astype(str)

data = df.groupby("Assets")["Approval"].mean()

xs = data.index 
ys = data

plt.figure(figsize=(8, 5))
bars = plt.bar(xs, ys, color='skyblue')
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2.,  
        height + 0.01,                     
        f'{height:.1%}',                   
        ha='center',                       
        va='bottom',                      
        fontsize=9                      
    )
plt.title("Approval Rate by Assets", fontsize=15)
plt.xlabel("Assets", fontsize=12)
plt.ylabel("Approval Rate", fontsize=12)

plt.ylim(0, 1)

plt.show()