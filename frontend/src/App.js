import { useState } from "react";

function App() {
  const [budget, setBudget] = useState("");
  const [result, setResult] = useState(null);

  // Function to call backend
  const getRecommendation = async () => {
    try {
      const response = await fetch("http://127.0.0.1:5000/recommend", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ budget })
      });

      const data = await response.json();
      setResult(data);
    } catch (error) {
      console.error("Error:", error);
    }
  };

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      
      {/* Title */}
      <h1>💡 Smart Budget Conscious Recommendation System</h1>

      {/* Input */}
      <input
        type="number"
        placeholder="Enter your budget"
        value={budget}
        onChange={(e) => setBudget(e.target.value)}
      />

      <br /><br />

      {/* Button */}
      <button onClick={getRecommendation}>
        Get Recommendation
      </button>

      {/* Output */}
      {result && (
        <div style={{ marginTop: "20px" }}>
          <h3>Results:</h3>
          <p>🍽 Best Option: {result.best}</p>
          <p>💰 Price: ₹{result.best_price}</p>
          <p>🥗 Healthy Option: {result.healthy}</p>
          <p>💪 Health Score: {result.health_score}</p>
        </div>
      )}
    </div>
  );
}

export default App;