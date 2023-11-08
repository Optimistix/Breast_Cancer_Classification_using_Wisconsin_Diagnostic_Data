import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pickle

df = pd.read_csv("Cancer_Data.csv")

# drop id and empty column
df.drop(['Unnamed: 32', "id"], axis=1, inplace=True)

# turn target variable into 1s and 0s
df.diagnosis =[1 if value == "M" else 0 for value in df.diagnosis]

# turn the target variable into categorical data
df['diagnosis'] = df['diagnosis'].astype('category',copy=False)

# Prepare the model
y = df["diagnosis"] # our target variable
X = df.drop(["diagnosis"], axis=1) # our predictors

# Split into training, validation and test datasets
X_full_train, X_test, y_full_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train, X_val, y_train, y_val = train_test_split(X_full_train, y_full_train, test_size=0.25, random_state=42)

# Train the best model on training data
model = LogisticRegression(C=25, solver="liblinear")
model.fit(X_train, y_train)

# Save the trained model using pickle
with open('model.bin', 'wb') as f_out:
   pickle.dump(model, f_out)
f_out.close()
