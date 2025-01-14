from flask import Flask, render_template, request, jsonify
import pickle

# Initialize Flask app
app = Flask(__name__)

# Load model and vectorizer from combined model.pkl file
with open("ml/model.pkl", "rb") as f:
    model, vectorizer = pickle.load(f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Get user input from form
    user_input = request.form["user_input"]
    
    # Transform input using vectorizer
    transformed_input = vectorizer.transform([user_input])
    
    # Make prediction
    prediction = model.predict(transformed_input)[0]
    sentiment = "Positive" if prediction == 1 else "Negative"
    
    # Return JSON response
    return jsonify({"sentiment": sentiment})

if __name__ == "__main__":
    app.run(debug=True)
