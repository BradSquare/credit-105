import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load dataset
credit = pd.read_csv("credit.csv")

# Countplot for Number of Existing Credits
credit_counts = credit["Num_Credits"].value_counts(normalize=True)
credit_counts = credit_counts.sort_index()
plt.figure(figsize=(8, 5))
ax = sns.barplot(x=credit_counts.index, y=credit_counts.values, palette="viridis")
plt.title("Distribution of Number of Existing Credits")
plt.xlabel("Number of Credits")
plt.ylabel("Percentage of Applicants")
plt.xticks(range(0, 5))  
plt.ylim(0, 1)

# Add percentages on top of the bars for Num_Credits
for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x() + p.get_width() / 2., height + 0.02,
            f'{height:.1%}', ha="center")

plt.show()

# Summary of Num_Credits
print(f"Num_Credits - Mean: {credit.Num_Credits.mean()}")
print(f"Num_Credits - Median: {credit.Num_Credits.median()}")
print(f"Num_Credits - Variance: {credit.Num_Credits.var()}")

# Filter out invalid values for Occupation (keep only 1, 2, 3, 4)
credit = credit[credit["Occupation"].isin([1, 2, 3, 4])]

# Define the occupation mapping
occupation_mapping = {
    1: "Unemployed/Unskilled - Non-Resident",
    2: "Unskilled - Resident",
    3: "Skilled Employee/Official",
    4: "Management/Self-Employed"
}

# Apply the mapping
credit["Occupation"] = credit["Occupation"].map(occupation_mapping)

# Countplot for Occupation 
occupation_counts = credit["Occupation"].value_counts(normalize=True)
plt.figure(figsize=(8, 5))
ax = sns.barplot(x=occupation_counts.index, y=occupation_counts.values, palette="viridis")
plt.title("Distribution of Occupation Types")
plt.xlabel("Occupation")
plt.ylabel("Percentage of Applicants")
plt.xticks(rotation=45, ha="right")  
plt.ylim(0, 1)  

# Add percentages on top of the bars
for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x() + p.get_width() / 2., height + 0.02,
            f'{height:.1%}', ha="center")

plt.show()

# Mode for Occupation
occupation_mode = credit["Occupation"].mode()[0]
print(f"Mode for Occupation: {occupation_mode}")

# Summary statistics for Occupation
#occupation_count = credit["Occupation"].value_counts()
#occupation_percentage = credit["Occupation"].value_counts(normalize=True) * 100

# Print the summary statistics
#print("Count of Occupation Types:")
#print(occupation_count)
#print("\nPercentage of Occupation Types:")
#print(occupation_percentage)

# Replace NaN values with 0 in Dependents
credit["Dependents"].fillna(0, inplace=True)

# Convert Dependents to integer type
credit["Dependents"] = credit["Dependents"].astype(int)

# Countplot for Number of Dependents
dependents_counts = credit["Dependents"].value_counts(normalize=True)
dependents_counts = dependents_counts.sort_index()
plt.figure(figsize=(8, 5))
ax = sns.barplot(x=dependents_counts.index, y=dependents_counts.values, palette="viridis")
plt.title("Distribution of Number of Dependents")
plt.xlabel("Number of Dependents")
plt.ylabel("Percentage of Applicants")

# Add percentages on top of the bars for Dependents
for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x() + p.get_width() / 2., height + 0.02,
            f'{height:.1%}', ha="center")

plt.show()

# Summary of Dependents
print(f"Dependents - Mean: {credit.Dependents.mean()}")
print(f"Dependents - Median: {credit.Dependents.median()}")
print(f"Dependents - Variance: {credit.Dependents.var()}")

# Correctly map Foreign_Worker values (1 = Yes, 2 = No)
# Filter out invalid values for Foreign_Worker (keep only 1 and 2)
credit = credit[credit["Foreign_Worker"].isin([1, 2])]

# Correctly map Foreign_Worker values
foreign_worker_mapping = {1: "Yes", 2: "No"}
credit["Foreign_Worker"] = credit["Foreign_Worker"].map(foreign_worker_mapping)

# Countplot for Foreign Worker Status
foreign_worker_counts = credit["Foreign_Worker"].value_counts(normalize=True)
plt.figure(figsize=(8, 5))
ax = sns.barplot(x=foreign_worker_counts.index, y=foreign_worker_counts.values, palette="viridis")
plt.title("Distribution of Foreign Worker Status")
plt.xlabel("Foreign Worker")
plt.ylabel("Percentage of Applicants")
plt.ylim(0, 1)

# Add percentages on top of the bars
for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x() + p.get_width() / 2., height + 0.02,
            f'{height:.1%}', ha="center")

plt.show()

# Mode for Foreign_Worker
foreign_worker_mode = credit["Foreign_Worker"].mode()[0]
print(f"Mode for Foreign Worker Status: {foreign_worker_mode}")


# Summary statistics for Foreign_Worker
#foreign_worker_summary = credit["Foreign_Worker"].value_counts(normalize=True) * 100
#count_summary = credit["Foreign_Worker"].value_counts()

# Print the summary statistics
#print("Count of Foreign Worker Status:")
#print(count_summary)
#print("\nPercentage of Foreign Worker Status:")
#print(foreign_worker_summary)

#bivariate analysis for Num_Credits and Approval
credit["Num_Credits"] = credit["Num_Credits"].astype(str)
data = credit.groupby("Num_Credits")["Approval"].mean()

plt.figure(figsize=(8, 5))
ax = sns.barplot(x=data.index, y=data.values, palette="viridis")
plt.title("Approval Rate by Number of Existing Credits")
plt.xlabel("Number of Credits")
plt.ylabel("Approval Rate")
plt.ylim(0, 1)

for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x() + p.get_width() / 2., height + 0.02, f'{height:.1%}', ha="center")

plt.show()

#bivariate analysis for Occupation and Approval
data = credit.groupby("Occupation")["Approval"].mean()

plt.figure(figsize=(8, 5))
ax = sns.barplot(x=data.index, y=data.values, palette="viridis")
plt.title("Approval Rate by Occupation")
plt.xlabel("Occupation")
plt.ylabel("Approval Rate")
plt.xticks(rotation=45, ha="right")  
plt.ylim(0, 1)

for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x() + p.get_width() / 2., height + 0.02, f'{height:.1%}', ha="center")

plt.show()

#bivariate analysis for Dependents and Approval
credit["Dependents"] = credit["Dependents"].astype(str)
data = credit.groupby("Dependents")["Approval"].mean()

plt.figure(figsize=(8, 5))
ax = sns.barplot(x=data.index, y=data.values, palette="viridis")
plt.title("Approval Rate by Number of Dependents")
plt.xlabel("Number of Dependents")
plt.ylabel("Approval Rate")
plt.ylim(0, 1)

for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x() + p.get_width() / 2., height + 0.02, f'{height:.1%}', ha="center")

plt.show()

#bivariate analysis for Foreign Worker and Approval
data = credit.groupby("Foreign_Worker")["Approval"].mean()

plt.figure(figsize=(8, 5))
ax = sns.barplot(x=data.index, y=data.values, palette="viridis")
plt.title("Approval Rate by Foreign Worker Status")
plt.xlabel("Foreign Worker")
plt.ylabel("Approval Rate")
plt.ylim(0, 1)

for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x() + p.get_width() / 2., height + 0.02, f'{height:.1%}', ha="center")

plt.show()


