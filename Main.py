import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df=pd.read_csv("CD.csv")

required = pd.read_csv("CD.csv", usecols = ['fraudulent','customer__customerIPAddress','orders__orderAmount','orders__orderState','paymentMethods__paymentMethodType','paymentMethods__paymentMethodProvider','transactions__transactionAmount','transactions__transactionFailed'])
required


# selecting only two columns data set and then visualising them wrt fraudulent
fraud_with_state=pd.read_csv("CD.csv",usecols=['fraudulent','orders__orderState'])
df["fraudulent"].fillna(" ", inplace = True) 
df["orders__orderState"].fillna(" ", inplace = True) 

fig, ax = plt.subplots()
ax.scatter(df['fraudulent'], df['orders__orderState'])
ax.set_title('Faudulant Dataset')
ax.set_xlabel('fraudulent')
ax.set_ylabel('orders__orderState')




# selecting only two columns data set and then visualising them wrt fraudulent
fraud_with_PayMethod=pd.read_csv("CD.csv",usecols=['fraudulent','paymentMethods__paymentMethodType'])
df["fraudulent"].fillna(" ", inplace = True) 
df["paymentMethods__paymentMethodType"].fillna(" ", inplace = True) 

fig, ax = plt.subplots()
ax.scatter(df['fraudulent'], df['paymentMethods__paymentMethodType'])
ax.set_title('Faudulant Dataset')
ax.set_xlabel('fraudulent')
ax.set_ylabel('paymentMethods__paymentMethodType')







# analysing required colomns with respect to fraudulent

fraud_with_amount=pd.read_csv('CD.csv',usecols=['fraudulent','paymentMethods__paymentMethodProvider','transactions__transactionAmount','transactions__transactionFailed'])



# 
# high correlation between feature like transaction amount , order amount and transactino failed or orde fulfilled . We will keep only one those features 

final=df.drop(['customer__customerEmail','customer__customerPhone','customer__customerDevice','customer__customerIPAddress'],axis=1)


import seaborn as sns
plt.figure(figsize=(20,20))
sns.heatmap(final.corr(),annot=True)