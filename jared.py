#jared's code 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("credit.csv")
# credit.info()

#percentage of missing values for each column
missing = df.apply(lambda x: x.isna().sum()/1000)
print(missing)

#check if ID are all unique values
id = df["ID"].unique()
print(len(id))

#find rows that are missing values for checking account
checking_account_missing = pd.isnull(df["Checking_Account"])
missing_ca = df[checking_account_missing]
print(missing_ca)

#find rows that are missing values for dependents
dependents_missing = pd.isnull(df["Dependents"])
missing_d = df[dependents_missing]
print(missing_d)

#fill in empty rows for checking account
df["Checking_Account"] = df["Checking_Account"].fillna(4)

#fill in empty rows for dependents
df["Dependents"] = df["Dependents"].fillna(0)
df.count()

#percentage of missing values for each column; check if there are still missing values
missing = df.apply(lambda x: x.isna().sum()/1000)
print(missing)

#check for outliers
# print(df[(np.abs(stats.zscore(df)) < 3).all(axis=1)])

#plot for personal status
print(f"Mode: {df['Personal_Status'].mode().iloc[0]}")

df["Personal_Status"] = df["Personal_Status"].astype(str)
data = df["Personal_Status"].value_counts(normalize=True)
data = data.sort_index(key=lambda x: x.astype(int))
xs = data.index
ys = data
plt.figure(figsize=(8,5))
plt.bar(xs, ys, color='skyblue')
plt.title("Number of Applicants by Personal Status", fontsize=15)
plt.ylabel("Number of Applicants", fontsize=12)
plt.xlabel("Personal Status", fontsize=12)
plt.show()

#plot for guarantors 
print(f"Mode: {df['Guarantors'].mode().iloc[0]}")

df["Guarantors"] = df["Guarantors"].astype(str)
data = df["Guarantors"].value_counts(normalize=True)
data = data.sort_index(key=lambda x: x.astype(int))
xs = data.index
ys = data
plt.figure(figsize=(8,5))
plt.bar(xs, ys, color='skyblue')
plt.title("Number of Applicants by Guarantors", fontsize=15)
plt.ylabel("Number of Applicants", fontsize=12)
plt.xlabel("Guarantors", fontsize=12)
plt.show()

#plot for residence_length
print(f"Mode: {df['Residence_Length'].mode().iloc[0]}")

df["Residence_Length"] = df["Residence_Length"].astype(str)
data = df["Residence_Length"].value_counts(normalize=True)
data = data.sort_index(key=lambda x: x.astype(int))
xs = data.index
ys = data
plt.figure(figsize=(8,5))
plt.bar(xs, ys, color='skyblue')
plt.title("Number of Applicants by Residence_Length", fontsize=15)
plt.ylabel("Number of Applicants", fontsize=12)
plt.xlabel("Residence_Length", fontsize=12)
plt.show()

#plot for assets
print(f"Mode: {df['Assets'].mode().iloc[0]}")


df["Assets"] = df["Assets"].astype(str)
data = df["Assets"].value_counts(normalize=True)
data = data.sort_index(key=lambda x: x.astype(int))
xs = data.index
ys = data
plt.figure(figsize=(8,5))
plt.bar(xs, ys, color='skyblue')
plt.title("Number of Applicants by Assets", fontsize=15)
plt.ylabel("Number of Applicants", fontsize=12)
plt.xlabel("Assets", fontsize=12)
plt.show()

#plot for assets
print(f"Mode: {df['Assets'].mode().iloc[0]}")


df["Assets"] = df["Assets"].astype(str)
data = df["Assets"].value_counts(normalize=True)
data = data.sort_index(key=lambda x: x.astype(int))
xs = data.index
ys = data
plt.figure(figsize=(8,5))
plt.bar(xs, ys, color='skyblue')
plt.title("Number of Applicants by Assets", fontsize=15)
plt.ylabel("Number of Applicants", fontsize=12)
plt.xlabel("Assets", fontsize=12)
plt.show()