#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# In[ ]:


# Data Retrieval
# df = retrieve_data_from_sql_or_spark()

# Dummy data for demonstration
data = {
    'income': np.random.normal(50000, 10000, 1000),
    'age': np.random.randint(20, 70, 1000),
    'homeownership': np.random.choice([0, 1], 1000)  # 0: Not a homeowner, 1: Homeowner
}
df = pd.DataFrame(data)


# In[ ]:


# 2. Data Preprocessing
# Drop any rows with missing values
df.dropna(inplace=True)


# In[ ]:


# Standardize the data
scaler = StandardScaler()
df[['income', 'age']] = scaler.fit_transform(df[['income', 'age']])


# In[ ]:


# 3. Model Training and Evaluation
# Split data into features (X) and target variable (y)
X = df[['income', 'age']]
y = df['homeownership']


# In[ ]:


# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# In[ ]:


# Choose a classification model (Logistic Regression in this example)
model = LogisticRegression()


# In[ ]:


# Train the model
model.fit(X_train, y_train)


# In[ ]:


# Make predictions on the testing set
y_pred = model.predict(X_test)


# In[ ]:


# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

