import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

credit = pd.read_csv("credit.csv")
# credit.info()

#percentage of missing values for each column
missing = credit.apply(lambda x: x.isna().sum()/1000)
# print(missing)

#check if ID are all unique values
id = credit["ID"].unique()
# print(len(id))

#find rows that are missing values for checking account
checking_account_missing = pd.isnull(credit["Checking_Account"])
missing_ca = credit[checking_account_missing]
# print(missing_ca)

#find rows that are missing values for dependents
dependents_missing = pd.isnull(credit["Dependents"])
missing_d = credit[dependents_missing]
# print(missing_d)

#fill in empty rows for checking account
credit["Checking_Account"].fillna(4, inplace=True)

#fill in empty rows for dependents
credit["Dependents"].fillna(0, inplace=True)

#percentage of missing values for each column; check if there are still missing values
missing = credit.apply(lambda x: x.isna().sum()/1000)
# print(missing)

#check for outliers
# print(credit[(np.abs(stats.zscore(credit)) < 3).all(axis=1)])

#get graph for distribution of checking account by type
checking_account_distribution = credit["Checking_Account"].value_counts(normalize=True).sort_index(ascending=True)
checking_account_distribution.plot(kind="bar", title="Checking_Account_Distribution")
plt.show()

#get graph for distribution of duration
duration_distribution = credit["Duration"].value_counts(normalize=True, bins=[x for x in range(3, 73, 3)]).sort_index(ascending=True)
duration_distribution.plot(kind="bar")
plt.show()

#get graph for distribution of payment status
payment_status_distribution = credit["Payment_Status"].value_counts(normalize=True).sort_index(ascending=True)
payment_status_distribution.plot(kind="bar")
plt.show()

#get graph for distribution of purpose
purpose_distribution = credit["Purpose"].value_counts(normalize=True).sort_index(ascending=True)
purpose_distribution.plot(kind="bar")
plt.show()

#bivariate analysis of checking account and approval
checking_account_approval = credit.set_index("Checking_Account")["Approval"].groupby("Checking_Account").mean()
checking_account_approval.plot(kind="bar", title="Checking_Account")
plt.show()

#bivariate analysis of duration and approval
duration_approval = credit.set_index(pd.cut(credit["Duration"], bins=[x for x in range(3, 73, 3)]))["Approval"].groupby("Duration").mean()
duration_approval.fillna(0,inplace=True)
duration_approval.plot(kind="line")
plt.show()

#bivariate analysis of purpose and approval
purpose_approval = credit.set_index("Purpose")["Approval"].groupby("Purpose").mean()
purpose_approval.plot(kind="bar")
plt.show()

#bivariate analysis of payment status and approval
payment_status_approval = credit.set_index("Payment_Status")["Approval"].groupby("Payment_Status").mean()
payment_status_approval.plot(kind="bar")
plt.show()

