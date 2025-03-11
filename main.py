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

# Countplot for Existing Credits (Proportion)
plt.figure(figsize=(8, 5))
ax = sns.countplot(data=credit, x="Existing_Credits", palette="viridis")
total = len(credit)  # Total number of applicants
for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x() + p.get_width() / 2, height, f'{height / total:.2f}', 
            ha="center", va="bottom", fontsize=10)  # Add proportion labels
ax.set_ylabel("Proportion of Applicants")
ax.set_yticks([i / 10 * total for i in range(11)])  # Adjust tick marks
ax.set_yticklabels([f"{i / 10:.1f}" for i in range(11)])  # Convert to proportions
plt.title("Count of Existing Credits")
plt.xlabel("Existing Credits")
plt.show()

# Display statistics (Only mode makes sense for categorical data)
print(f"Existing Credits - Mode: {credit['Existing_Credits'].mode()[0]}")

# Countplot for Housing Type (Proportion)
plt.figure(figsize=(8, 5))
ax = sns.countplot(data=credit, x="Housing_Type", palette="coolwarm")
total = len(credit)
for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x() + p.get_width() / 2, height, f'{height / total:.2f}', 
            ha="center", va="bottom", fontsize=10)  # Add proportion labels
ax.set_ylabel("Proportion of Applicants")
ax.set_yticks([i / 10 * total for i in range(11)])
ax.set_yticklabels([f"{i / 10:.1f}" for i in range(11)])
plt.title("Count of Housing Types")
plt.xlabel("Housing Type")
plt.show()

# Display statistics (Mode only for categorical)
print(f"Housing Type - Mode: {credit['Housing_Type'].mode()[0]}")

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

