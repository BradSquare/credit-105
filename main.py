import matplotlib.pyplot as plt
import seaborn as sns

# Set a consistent style
sns.set_style("whitegrid")

# Histogram for Age (Proportion)
plt.figure(figsize=(8, 5))
sns.histplot(credit["Age"], bins=20, kde=True, color="skyblue", stat="probability")
plt.title("Distribution of Age")
plt.xlabel("Age")
plt.ylabel("Proportion of Applicants")
plt.show()

# Histogram for Credit Rating (Proportion)
plt.figure(figsize=(8, 5))
sns.histplot(credit["Credit_Rating"], bins=20, kde=True, color="orange", stat="probability")
plt.title("Distribution of Credit Rating")
plt.xlabel("Credit Rating")
plt.ylabel("Proportion of Applicants")
plt.show()

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

# Countplot for Housing Type (Proportion)
plt.figure(figsize=(8, 5))
ax = sns.countplot(data=credit, x="Housing_Type", palette="viridis")
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
