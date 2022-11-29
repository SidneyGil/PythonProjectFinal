from flask import Flask, render_template

app = Flask(__name__)
# Function to read in details for page

@app.route('/')
def homePage():
    return render_template("index.html")
