# Import required libraries
from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Allow React frontend to connect

# Load dataset
data = pd.read_csv("data/food.csv")

# Home route (for testing)
@app.route('/')
def home():
    return "Smart Budget Conscious Recommendation System Backend 🚀"

# Recommendation logic
def recommend_food(budget):
    # Filter items within budget
    filtered = data[data['price'] <= budget]

    # If nothing found
    if filtered.empty:
        return None, None

    # Best option → high health_score + low price
    best = filtered.sort_values(
        by=['health_score', 'price'],
        ascending=[False, True]
    ).iloc[0]

    # Healthiest option → highest health_score
    healthy = filtered.sort_values(
        by='health_score', ascending=False
    ).iloc[0]

    return best, healthy


# API route
@app.route('/recommend', methods=['POST'])
def recommend():
    # Get data from frontend
    budget = int(request.json['budget'])

    # Call logic
    best, healthy = recommend_food(budget)

    if best is None:
        return jsonify({"message": "No items within budget"})

    # Send response
    return jsonify({
        "best": best['name'],
        "best_price": int(best['price']),
        "healthy": healthy['name'],
        "health_score": int(healthy['health_score'])
    })


# Run server
if __name__ == '__main__':
    app.run(debug=True)