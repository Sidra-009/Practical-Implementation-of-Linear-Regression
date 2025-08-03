#!/usr/bin/env python
# coding: utf-8

# In[65]:


print("Sidra Saqlain")
print("Linaer regression Practical Implemetation")


# In[116]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns


# In[109]:


dataset = pd.read_csv("Salary_Data.csv")
dataset


# In[70]:


#checking for null values
df.isnull().sum()


# In[71]:


#checking for correlation
df.corr()


# In[117]:


x = dataset.iloc[:, :-1].values
y = dataset.iloc[:,1].values


# In[119]:


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.30,random_state=42)


# In[77]:


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
x_train= scaler.fit_transform(x_train)
x_test = scaler.fit_transform(x_test)


# In[90]:


from sklearn.linear_model import LinearRegression
regression = LinearRegression()
regression.fit(x_train, y_train)


# In[85]:


coeff = regression.coef_
coeff
intercept = regression.intercept_
intercept
print("Coefficient/ Slope:",coeff)
print("intercept:",intercept)


# In[94]:


y_pred = regression.predict(x_test)
print("Predicted Salaries (First 5 ):",y_pred[:5])


# In[98]:


from sklearn.metrics import mean_squared_error, r2_score
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test,y_pred)
print("MSE:",mse)
print("R Square score:",r2)


# In[ ]:





# In[123]:


#plt.figure(figsize=(8,6))
plt.scatter(y_test,y_pred, color='red', edgecolor='g')
plt.plot(x_train, regression.predict(x_train),color='yellow')
plt.xlabel("Actual Salary")
plt.xlabel("Predicted Salary")
plt.title("Actual vs Predicted Salary")
plt.grid(True)
plt.show()


# In[124]:


sns.displot(y_pred-y_test,kind='kde',color='green')
plt.title("distribution of Residuals (Errors)")
plt.xlabel("Prediction Error")
plt.show()
print("Linear Regression Practical Implementation Completed Sucessfully")


# In[ ]:




