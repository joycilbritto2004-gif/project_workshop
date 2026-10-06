from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


# -----------------------------
# Home Page
# -----------------------------
@app.route("/")
def home():
    return """
    <h1>Welcome to My Flask Application</h1>
    <p>This is the home page.</p>
    <a href="/about">Go to About Page</a><br>
    <a href="/contact">Go to Contact Page</a><br>
    <a href="/hello/Joy">Say Hello</a>
    """


# -----------------------------
# About Page
# -----------------------------
@app.route("/about")
def about():
    return """
    <h1>About Us</h1>
    <p>This application is developed using Python and Flask.</p>
    <p>Flask is a lightweight web framework for Python.</p>
    """


# -----------------------------
# Contact Page
# -----------------------------
@app.route("/contact")
def contact():
    return """
    <h1>Contact Us</h1>
    <p>Email: example@gmail.com</p>
    <p>Phone: 9876543210</p>
    """


# -----------------------------
# Dynamic URL
# -----------------------------
@app.route("/hello/<name>")
def hello(name):
    return f"""
    <h1>Hello {name}!</h1>
    <p>Welcome to the Flask application.</p>
    """


# -----------------------------
# Simple Calculation
# -----------------------------
@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    result = a + b

    return f"""
    <h1>Addition</h1>
    <p>{a} + {b} = {result}</p>
    """


# -----------------------------
# User Form
# -----------------------------
@app.route("/form", methods=["GET", "POST"])
def form():

    if request.method == "POST":

        name = request.form.get("name")
        email = request.form.get("email")

        return f"""
        <h1>Form Submitted Successfully</h1>
        <p>Name: {name}</p>
        <p>Email: {email}</p>
        """

    return """
    <h1>User Form</h1>

    <form method="POST">

        <label>Name:</label><br>
        <input type="text" name="name" required><br><br>

        <label>Email:</label><br>
        <input type="email" name="email" required><br><br>

        <button type="submit">Submit</button>

    </form>
    """


# -----------------------------
# JSON API
# -----------------------------
@app.route("/api")
def api():

    data = {
        "name": "Flask Application",
        "status": "success",
        "message": "API is working correctly"
    }

    return jsonify(data)


# -----------------------------
# Calculator API
# -----------------------------
@app.route("/api/add", methods=["POST"])
def api_add():

    data = request.get_json()

    number1 = data.get("number1")
    number2 = data.get("number2")

    result = number1 + number2

    return jsonify({
        "number1": number1,
        "number2": number2,
        "result": result
    })


# -----------------------------
# Error Handling
# -----------------------------
@app.errorhandler(404)
def page_not_found(error):

    return """
    <h1>404 - Page Not Found</h1>
    <p>The page you are looking for does not exist.</p>
    <a href="/">Go to Home</a>
    """, 404


# -----------------------------
# Run Application
# -----------------------------
if __name__ == "__main__":

    print("Starting Flask Application...")

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )