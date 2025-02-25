import numpy as np
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = {
    "Bedrooms": [5, 3, 6, 6, 1],
    "Toilets": [5, 3, 3, 6, 1],
    "Parking_Space": [2, 1, 1, 1, 0],
    "Price": [2000000, 1000000, 1700000, 2500000, 200000]
}

df = pd.DataFrame(data)
print(df.head())

x = df[['Bedrooms', 'Toilets', 'Parking Space']]
y = df['Price']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(x_train, y_train)

joblib.dump(model, "predictor/ml_model.pkl")
print("model saved successfully")