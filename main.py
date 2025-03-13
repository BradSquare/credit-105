import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load dataset
credit = pd.read_csv("credit.csv")

# Set a consistent style
sns.set_style("whitegrid")
#####################################################################Denzyl##################################################################################################################
# Histogram for Age (Proportion)
plt.figure(figsize=(8, 5))
sns.histplot(credit["Age"], bins=20, kde=True, color="skyblue", stat="probability")
plt.title("Distribution of Age")
plt.xlabel("Age")
plt.ylabel("Proportion of Applicants")
plt.show()

# Display statistics
print(f"Age - Mean: {credit['Age'].mean():.2f}")
print(f"Age - Median: {credit['Age'].median():.2f}")
print(f"Age - Mode: {credit['Age'].mode()[0]:.2f}")


# Histogram for Credit Rating (Proportion)
plt.figure(figsize=(8, 5))
sns.histplot(credit["Credit_Rating"], bins=20, kde=True, color="orange", stat="probability")
plt.title("Distribution of Credit Rating")
plt.xlabel("Credit Rating")
plt.ylabel("Proportion of Applicants")
plt.show()

# Display statistics
print(f"Credit Rating - Mean: {credit['Credit_Rating'].mean():.2f}")
print(f"Credit Rating - Median: {credit['Credit_Rating'].median():.2f}")
print(f"Credit Rating - Mode: {credit['Credit_Rating'].mode()[0]:.2f}")


# plot for Existing Credits (normalized)
df["Existing_Credits"] = df["Existing_Credits"].astype(int)
data = df.groupby("Existing_Credits").size()

# Normalize the values by dividing by the total count
ys = data / data.sum()
xs = data.index
plt.figure(figsize=(8, 5))

# Set all bars to a specific color from the 'viridis' colormap
plt.bar(xs, ys, color=plt.cm.viridis(0.5))  # 0.5 for a middle color from the colormap
plt.title("Proportion of Applicants by Existing Credits", fontsize=15)
plt.xlabel("Existing Credits", fontsize=12)
plt.ylabel("Proportion of Applicants", fontsize=12)
plt.xticks(range(1, 4))
plt.show()

# Display statistics (Only mode makes sense for categorical data)
print(f"Existing Credits - Mode: {credit['Existing_Credits'].mode()[0]}")

# Countplot for Housing Type (Proportion)
df["Housing_Type"] = df["Housing_Type"].astype(int)
data = df.groupby("Housing_Type").size()

# Normalize the values by dividing by the total count
ys = data / data.sum()
xs = data.index
plt.figure(figsize=(8, 5))

# Set all bars to a specific color from the 'viridis' colormap
plt.bar(xs, ys, color=plt.cm.viridis(0.5))  # 0.5 for a middle color from the colormap

plt.title("Proportion of Applicants by Housing Type", fontsize=15)
plt.xlabel("Housing Type", fontsize=12)
plt.ylabel("Proportion of Applicants", fontsize=12)
plt.xticks(range(1, 4))
plt.show()

# Display statistics (Mode only for categorical)
print(f"Housing Type - Mode: {credit['Housing_Type'].mode()[0]}")

# Approval Rate vs. Age
approval_rate_by_age = credit.groupby("Age")["Approved"].mean()
plt.figure(figsize=(8, 5))
sns.lineplot(x=approval_rate_by_age.index, y=approval_rate_by_age.values, marker="o", color="royalblue")
plt.title("Approval Rate vs. Age")
plt.xlabel("Age")
plt.ylabel("Approval Rate")
plt.ylim(0, 1)
plt.grid(True)
plt.show()

# Approval Rate vs. Credit Rating
approval_rate_by_credit = credit.groupby("Credit_Rating")["Approved"].mean()
plt.figure(figsize=(8, 5))
sns.lineplot(x=approval_rate_by_credit.index, y=approval_rate_by_credit.values, marker="o", color="orange")
plt.title("Approval Rate vs. Credit Rating")
plt.xlabel("Credit Rating")
plt.ylabel("Approval Rate")
plt.ylim(0, 1)
plt.grid(True)
plt.show()

# Approval Rate for Existing Credits
df["Existing_Credits"] = df["Existing_Credits"].astype(int)

# Compute approval rate instead of count
data = df.groupby("Existing_Credits")["Approved"].mean()

# Get x (categories) and y (approval rate)
ys = data  # Already normalized as mean (between 0 and 1)
xs = data.index

plt.figure(figsize=(8, 5))

# Set all bars to a specific color from the 'viridis' colormap
plt.bar(xs, ys, color=plt.cm.viridis(0.5))  # 0.5 for a middle color from the colormap

plt.title("Approval Rate by Existing Credits", fontsize=15)
plt.xlabel("Existing Credits", fontsize=12)
plt.ylabel("Approval Rate", fontsize=12)
plt.ylim(0, 1)  # Approval rate is always between 0 and 1
plt.xticks(range(1, 4))  # Adjust based on unique categories
plt.show()

# Display statistics
print(f"Existing Credits - Mode: {df['Existing_Credits'].mode()[0]}")

# Approval Rate for Housing Type
df["Housing_Type"] = df["Housing_Type"].astype(int)

# Compute approval rate instead of count
data = df.groupby("Housing_Type")["Approved"].mean()

# Get x (categories) and y (approval rate)
ys = data  # Already normalized as mean (between 0 and 1)
xs = data.index

plt.figure(figsize=(8, 5))

# Set all bars to a specific color from the 'viridis' colormap
plt.bar(xs, ys, color=plt.cm.viridis(0.5))  # 0.5 for a middle color from the colormap

plt.title("Approval Rate by Housing Type", fontsize=15)
plt.xlabel("Housing Type", fontsize=12)
plt.ylabel("Approval Rate", fontsize=12)
plt.ylim(0, 1)  # Approval rate is always between 0 and 1
plt.xticks(range(1, 4))  # Adjust based on unique categories
plt.show()

# Display statistics
print(f"Housing Type - Mode: {df['Housing_Type'].mode()[0]}")

#####################################################################Priya##################################################################################################################
# Countplot for Number of Existing Credits
credit_counts = credit["Num_Credits"].value_counts(normalize=True)
credit_counts = credit_counts.sort_index()
plt.figure(figsize=(8, 5))
ax = sns.barplot(x=credit_counts.index, y=credit_counts.values, palette="viridis")
plt.title("Distribution of Number of Existing Credits")
plt.xlabel("Number of Credits")
plt.ylabel("Proportion")
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

# Define the occupation mapping
occupation_mapping = {
    1: "Unemployed/Unskilled - Non-Resident",
    2: "Unskilled - Resident",
    3: "Skilled Employee/Official",
    4: "Management/Self-Employed"
}

credit["Occupation"] = credit["Occupation"].map(occupation_mapping)

# Countplot for Occupation 
occupation_counts = credit["Occupation"].value_counts(normalize=True)
plt.figure(figsize=(8, 5))
ax = sns.barplot(x=occupation_counts.index, y=occupation_counts.values, palette="viridis")
plt.title("Distribution of Occupation Types")
plt.xlabel("Occupation")
plt.ylabel("Proportion")
plt.xticks(rotation=45, ha="right")  
plt.ylim(0, 1)  

# Add percentages on top of the bars for Occupation
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
plt.ylabel("Proportion")

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
credit["Foreign_Worker"] = credit["Foreign_Worker"].map({1: "Yes", 2: "No"})

# Countplot for Foreign Worker Status
foreign_worker_counts = credit["Foreign_Worker"].value_counts(normalize=True)
plt.figure(figsize=(8, 5))
ax = sns.barplot(x=foreign_worker_counts.index, y=foreign_worker_counts.values, palette="viridis")
plt.title("Distribution of Foreign Worker Status")
plt.xlabel("Foreign Worker")
plt.ylabel("Proportion")

# Add percentages on top of the bars for Foreign Worker
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

