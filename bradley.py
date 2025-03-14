# summary statistics for amount
print(f"Mean : {credit.Amount.mean()}")
print(f"Median : {credit.Amount.median()}")
print(f"Variance : {credit.Amount.var()}")

# Summary of Num_Credits
print(f"Num_Credits - Mean: {credit.Num_Credits.mean()}")
print(f"Num_Credits - Median: {credit.Num_Credits.median()}")
print(f"Num_Credits - Variance: {credit.Num_Credits.var()}")

################################################################################################################

# plot for amount
# Set a consistent style
sns.set_style("whitegrid")

# Histogram for Age
plt.figure(figsize=(8, 5))
sns.histplot(credit["Amount"], bins=5, kde=True, color=plt.cm.viridis(0.5))
plt.title("Distribution of Amount")
plt.xlabel("Amount")
plt.ylabel("Count")
plt.show()

################################################################################################################

# plot for approval rate and amount
# Set a consistent style
sns.set_style("whitegrid")

# Create custom bins as per your requirement
bins = [0, 3000, 6000, 9000, 12000, np.inf]  # np.inf represents greater than 12000

# Bin the 'Amount' values based on the custom bins
credit['Amount_Binned'] = pd.cut(credit['Amount'], bins=bins, right=False)

# Define custom labels for the bins
bin_labels = ['0 to 2999', '3000 to 5999', '6000 to 8999', '9000 to 11999', '12000 and above']

# Assign custom labels to the binned data
credit['Amount_Binned'] = credit['Amount_Binned'].cat.rename_categories(bin_labels)

# Calculate the approval rate for each bin, specifying observed=False to avoid FutureWarning
approval_rate_by_bin = credit.groupby('Amount_Binned', observed=False)['Approval'].mean().reset_index()

# Plotting the barplot for approval rate across the binned amounts
plt.figure(figsize=(8, 5))
sns.barplot(data=approval_rate_by_bin, x='Amount_Binned', y='Approval', color=plt.cm.viridis(0.5))

# Add title and labels
plt.title("Approval Rate by Amount", fontsize=15)
plt.xlabel("Amount", fontsize=12)
plt.ylabel("Approval Rate", fontsize=12)

# Rotate x-ticks for better readability
plt.xticks(rotation=45)
plt.ylim(0, 1)  # Ensure the y-axis is between 0 and 1 for approval rate
    
plt.show()

################################################################################################################

# summary statistics for savings account
print(f"Mode : {credit.Savings_Account.mode()}")

################################################################################################################

# plot for savings_account (normalized)
data = credit.groupby("Savings_Account").size()

# Normalize the values by dividing by the total count
ys = data / data.sum()

xs = data.index

plt.figure(figsize=(8, 5))
ax = plt.bar(xs, ys, color=plt.cm.viridis(0.5))
plt.title("Distribution of Savings Account", fontsize=15)
plt.ylabel("Proportion of Applicants", fontsize=12)
plt.xlabel("Savings Account", fontsize=12)
plt.ylim(0, 0.8)

for p in ax:
    height = p.get_height()
    plt.text(p.get_x() + p.get_width() / 2., height + 0.02,  # Adjust vertical positioning with + 0.02
             f'{height:.1%}', ha="center", fontsize=10)  # Formatting to show percentage

plt.show()

################################################################################################################

# plot for savings_account and approval rate
credit["Savings_Account"] = credit["Savings_Account"].astype(str)

data = credit.groupby("Savings_Account")["Approval"].mean()

xs = data.index
ys = data

plt.figure(figsize=(8, 5))
plt.bar(xs, ys, color=plt.cm.viridis(0.5))
plt.title("Approval Rate by Savings Account", fontsize=15)
plt.xlabel("Savings Account", fontsize=12)
plt.ylabel("Approval Rate", fontsize=12)

plt.ylim(0, 1)

plt.show()

################################################################################################################

# summary statistics for employment
print(f"Mode : {credit.Employment.mode()}")
credit.Employment.describe()

################################################################################################################

# plot for employment (normalized)
data = credit.groupby("Employment").size()

# Normalize the values by dividing by the total count
ys = data / data.sum()

xs = data.index

plt.figure(figsize=(8, 5))
ax = plt.bar(xs, ys, color=plt.cm.viridis(0.5))
plt.title("Distribution of Employment", fontsize=15)
plt.xlabel("Employment", fontsize=12)
plt.ylabel("Proportion of Applicants", fontsize=12)

plt.ylim(0, 0.4)

for p in ax:
    height = p.get_height()
    plt.text(p.get_x() + p.get_width() / 2., height + 0.02,  # Adjust vertical positioning with + 0.02
             f'{height:.1%}', ha="center", fontsize=10)  # Formatting to show percentage

plt.show()

################################################################################################################

#plot for employment and approval rate
credit["Employment"] = credit["Employment"].astype(str)

data = credit.groupby("Employment")["Approval"].mean()

xs = data.index
ys = data

plt.figure(figsize=(8, 5))
plt.bar(xs, ys, color=plt.cm.viridis(0.5))
plt.title("Approval Rate by Employment", fontsize=15)
plt.xlabel("Employment", fontsize=12)
plt.ylabel("Approval Rate", fontsize=12)

plt.ylim(0, 1)

plt.show()

################################################################################################################

#summary statistics for installment
print(f"Mean : {credit.Installment.mean()}")
print(f"Median : {credit.Installment.median()}")
print(f"Mode : {credit.Installment.mode()}")
print(f"Variance : {credit.Installment.var()}")
credit.Installment.describe()

################################################################################################################

# plot for installment (normalized)
credit["Installment"] = credit["Installment"].astype(int)

data = credit.groupby("Installment").size()

# Normalize the values by dividing by the total count
ys = data / data.sum()

xs = data.index

plt.figure(figsize=(8, 5))

# Set all bars to a specific color from the 'viridis' colormap
ax = plt.bar(xs, ys, color=plt.cm.viridis(0.5))  # 0.5 for a middle color from the colormap

plt.title("Distribution of Installment Rate", fontsize=15)
plt.xlabel("Installment Rate", fontsize=12)
plt.ylabel("Proportion of Applicants", fontsize=12)

plt.xticks(range(1, 5))

plt.ylim(0, 0.6)

for p in ax:
    height = p.get_height()
    plt.text(p.get_x() + p.get_width() / 2., height + 0.02,  # Adjust vertical positioning with + 0.02
             f'{height:.1%}', ha="center", fontsize=10)  # Formatting to show percentage

plt.show()

################################################################################################################

# plot for installment and approval rate
# Group by Installment and calculate the approval rate (mean of Approval)
approval_rate_by_installment = credit.groupby("Installment")["Approval"].mean()

# Normalize the approval rates (optional, if you want to show them in proportion, but here the mean of approval is fine)
approval_rate_by_installment = approval_rate_by_installment

# Plotting the bar chart for approval rate by installment rate
plt.figure(figsize=(8, 5))

# Set all bars to a specific color from the 'viridis' colormap
plt.bar(approval_rate_by_installment.index, approval_rate_by_installment, color=plt.cm.viridis(0.5))  # 0.5 for a middle color

# Add title and labels
plt.title("Approval Rate by Installment Rate", fontsize=15)
plt.xlabel("Installment Rate", fontsize=12)
plt.ylabel("Approval Rate", fontsize=12)

# Set x-ticks
plt.xticks(range(1, 5))

# Show the plot
plt.show()

################################################################################################################
# LINE GRAPH AlTERNATIVES FOR INSTALLMENT
################################################################################################################
# plot for installment rate
# Normalize the values by dividing by the total count
data = credit.groupby("Installment").size()
ys = data / data.sum()

# x-values are the Installment rates
xs = data.index

plt.figure(figsize=(8, 5))

# Plot the line graph (use 'o' marker to indicate points)
ax = plt.plot(xs, ys, marker='o', color=plt.cm.viridis(0.5), linestyle='-', linewidth=2)

# Add title and labels
plt.title("Distribution of Installment Rate", fontsize=15)
plt.xlabel("Installment Rate", fontsize=12)
plt.ylabel("Proportion of Applicants", fontsize=12)

# Adding percentages on top of each point in the line graph
for i, v in enumerate(ys):
    plt.text(xs[i], v + 0.02, f'{v:.1%}', ha='center', fontsize=10)  # Adjust vertical position with + 0.02

# Set y-axis limit (optional, depending on your data)
plt.ylim(0, 0.6)

# Show the plot
plt.show()

################################################################################################################

# plot for installment and approval rate
credit["Installment"] = credit["Installment"].astype(str)

data = credit.groupby("Installment")["Approval"].mean()

xs = data.index
ys = data

plt.figure(figsize=(8, 5))
plt.plot(xs, ys, marker='o', color=plt.cm.viridis(0.5), linewidth=2)
plt.title("Approval Rate by Installment Rate", fontsize=15)
plt.xlabel("Installment Rate", fontsize=12)
plt.ylabel("Approval Rate", fontsize=12)

plt.ylim(0, 1)

plt.show()