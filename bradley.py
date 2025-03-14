# bivariate analysis of amount and approval

bins = [0, 3000, 6000, 9000, 12000, np.inf]  

credit['Amount_Binned'] = pd.cut(credit['Amount'], bins=bins, right=False)
bin_labels = ['0 to 2999', '3000 to 5999', '6000 to 8999', '9000 to 11999', '12000 and above']
credit['Amount_Binned'] = credit['Amount_Binned'].cat.rename_categories(bin_labels)
approval_rate_by_bin = credit.groupby('Amount_Binned', observed=False)['Approval'].mean().reset_index()
plt.figure(figsize=(8, 5))

x = approval_rate_by_bin['Amount_Binned']
y = approval_rate_by_bin['Approval']

plt.bar(x, y, color=plt.cm.viridis(0.5))
plt.title("Approval Rate by Amount", fontsize=15)
plt.xlabel("Amount", fontsize=12)
plt.ylabel("Approval Rate", fontsize=12)
plt.xticks(rotation=45)
plt.ylim(0, 1)  # Ensure the y-axis is between 0 and 1 for approval rate

plt.show()




# bivariate analysis of savings account and approval
df["Savings_Account"] = df["Savings_Account"].astype(str)

data = df.groupby("Savings_Account")["Approval"].mean()

xs = data.index
ys = data

plt.figure(figsize=(8, 5))
ax = plt.bar(xs, ys, color=plt.cm.viridis(0.5))
plt.title("Approval Rate by Savings Account")
plt.xlabel("Savings Account")
plt.ylabel("Approval Rate")

for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x() + p.get_width() / 2., height + 0.02, f'{height:.1%}', ha="center")

plt.ylim(0, 1)

plt.show()




#bivariate analysis of employment and approval
credit["Employment"] = credit["Employment"].astype(str)

data = credit.groupby("Employment")["Approval"].mean()

xs = data.index
ys = data

fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(xs, ys, color=plt.cm.viridis(0.5))

ax.set_title("Approval Rate by Employment")
ax.set_xlabel("Employment")
ax.set_ylabel("Approval Rate")

for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height:.1%}', 
                (bar.get_x() + bar.get_width() / 2., height), 
                textcoords="offset points", 
                xytext=(0, 5), 
                ha="center")

ax.set_ylim(0, 1)

plt.show()


#bivariate analysis of installment and approval
credit["Installment"] = credit["Installment"].astype(str)

data = credit.groupby("Installment")["Approval"].mean()

xs = data.index
ys = data

plt.figure(figsize=(8, 5))
plt.plot(xs, ys, marker='o', color=plt.cm.viridis(0.5), linewidth=2)


for i, (x, y) in enumerate(zip(xs, ys)):
    plt.text(x, y + 0.03, f'{y:.1%}', ha='center', va='bottom', fontsize=10)  # y + 0.03 to move text higher

plt.title("Approval Rate by Installment Rate", fontsize=15)
plt.xlabel("Installment Rate", fontsize=12)
plt.ylabel("Approval Rate", fontsize=12)

plt.ylim(0, 1)

plt.show()
