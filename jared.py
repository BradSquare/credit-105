import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

#CLEANING DATA
#Read File  
credit = pd.read_csv("credit.csv")

#Percentage of missing values for each column
missing = credit.apply(lambda x: x.isna().sum()/1000)
#print(missing)

#Check if ID are all unique values
id = credit["ID"].unique()
#print(len(id))

#Find rows that are missing values for checking account
checking_account_missing = pd.isnull(credit["Checking_Account"])
missing_ca = credit[checking_account_missing]
#print(missing_ca)

#find rows that are missing values for dependents
dependents_missing = pd.isnull(credit["Dependents"])
missing_d = credit[dependents_missing]
#print(missing_d)

#fill in empty rows for checking account
credit["Checking_Account"].fillna(4, inplace=True)

#fill in empty rows for dependents
credit["Dependents"].fillna(0, inplace=True)

#percentage of missing values for each column; check if there are still missing values
missing = credit.apply(lambda x: x.isna().sum()/1000)
#print(missing)

#check for outliers
print(credit[(np.abs(stats.zscore(credit)) < 3).all(axis=1)])




#CHECKING INVALID VALUES  
#Evaluating Invalid Data (e.g. out of the range) from Personal_Status, Guarantors, Residence_Length and Assets

# Find invalid values (less than 1 or greater than 4) for Personal_Status
invalid_values = credit[(credit["Personal_Status"] <= 0) | (credit["Personal_Status"] > 4)]

# Print results
if not invalid_values.empty:
    print("Invalid Personal_Status values found:")
    print(invalid_values)
else:
    print("All Personal_Status values are valid.")

# Find invalid values (less than 1 or greater than 3) for Guarantors
invalid_values = credit[(credit["Guarantors"] < 1) | (credit["Guarantors"] > 3)]

# Print results
if not invalid_values.empty:
    print("Invalid Guarantors values found:")
    print(invalid_values)
else:
    print("All Guarantors values are valid.")


# Find invalid values (less than 1 or greater than 4) for Residence_Length
invalid_values = credit[(credit["Residence_Length"] < 1) | (credit["Residence_Length"] > 4)]

# Print results
if not invalid_values.empty:
    print("Invalid Residence_Length values found:")
    print(invalid_values)
    
    # Calculate the mode of Residence_Length (excluding invalid values)
    valid_residence = credit[(credit["Residence_Length"] >= 1) & (credit["Residence_Length"] <= 4)]["Residence_Length"]
    residence_mode = valid_residence.mode()[0]  # mode() returns a Series, so we get the first value

    # Replace invalid values with the mode
    credit.loc[(credit["Residence_Length"] < 1) | (credit["Residence_Length"] > 4), "Residence_Length"] = residence_mode

# Re-evaluate Residence_Length for any Invalid values
invalid_values = credit[(credit['Residence_Length'] < 1) | (credit['Residence_Length'] > 4)]

# Print results
if not invalid_values.empty:
    print("Invalid Residence_Length values found:")
    print(invalid_values)
else:
    print("All Residence_Length values are valid.")

# Find invalid values (less than 1 or greater than 4) for Assets
credit['Assets'] = pd.to_numeric(credit['Assets'])
invalid_values = credit[(credit["Assets"] < 1) | (credit["Assets"] > 4)]

# Print results
if not invalid_values.empty:
    print("Invalid Assets values found:")
    print(invalid_values)
else:
    print("All Assets values are valid.")





#PLOTTING UNIVARIATE
#plot for Personal_Status
print(f"Mode: {credit['Personal_Status'].mode().iloc[0]}")

credit["Personal_Status"] = credit["Personal_Status"].astype(str)
data = credit["Personal_Status"].value_counts(normalize=True)
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
print(f"Mode: {credit['Guarantors'].mode().iloc[0]}")

credit["Guarantors"] = credit["Guarantors"].astype(str)
data = credit["Guarantors"].value_counts(normalize=True)
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
print(f"Mode: {credit['Residence_Length'].mode().iloc[0]}")

credit["Residence_Length"] = credit["Residence_Length"].astype(str)
data = credit["Residence_Length"].value_counts(normalize=True)
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
print(f"Mode: {credit['Assets'].mode().iloc[0]}")

credit["Assets"] = credit["Assets"].astype(str)
data = credit["Assets"].value_counts(normalize=True)
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
credit["Personal_Status"] = credit["Personal_Status"].astype(str)

data = credit.groupby("Personal_Status")["Approval"].mean()

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
credit["Guarantors"] = credit["Guarantors"].astype(str)

data = credit.groupby("Guarantors")["Approval"].mean()

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
credit["Residence_Length"] = credit["Residence_Length"].astype(str)

data = credit.groupby("Residence_Length")["Approval"].mean()

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
credit["Assets"] = credit["Assets"].astype(str)

data = credit.groupby("Assets")["Approval"].mean()

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