# Import libraries
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Load dataset
data = pd.read_csv("data/food.csv")

# Features (inputs)
X = data[['calories', 'protein', 'price']]

# Label (healthy or not)
y = data['health_score'] >= 7

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# Function to predict
def predict_health(calories, protein, price):
    return model.predict([[calories, protein, price]])