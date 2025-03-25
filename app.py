from flask import Flask, render_template
from static.journal import app as journal_app

#name tells flask to use this as the main application

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  #loads HTML file 

@app.route("/chatbot")  #chatbot route
def chatbot():
    return "This is the chatbot page!"

@app.route("/journal")  #journaling route
def journal():
    return render_template("journal.html")

if __name__ == "__main__":  # only runs Flask if script is executed directly
    app.run(debug=True)  #starts the Flask web server and automates code changes

