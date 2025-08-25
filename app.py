from flask import Flask, render_template, request, jsonify, url_for, redirect, session
from backend.journal import load_entries, save_entry
from backend.users import add_user, verify_user
import os

#name tells flask to use this as the main application

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/")
def home():
    return render_template("index.html")  #loads HTML file 

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if add_user(username, password):
            return redirect(url_for("login"))
        return "Username already exists!"
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if verify_user(username, password):
            session["user"] = username
            return redirect(url_for("journal"))
        return "Invalid credentials!"
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

@app.route("/chatbot")  #chatbot route
def chatbot():
    return "This is the chatbot page!"


@app.route("/journal", methods=["GET", "POST"])
def journal():
    if request.method == "POST":
        entry_text = request.get_json().get("entry", "").strip()
        if not entry_text:
            return jsonify({"error": "Entry cannot be empty"}), 400

        #Save to journal.json
        save_entry(entry_text)
        return jsonify({"message": "Journal entry saved!"})
    
    #GET: load entries from JSON file
    entries = load_entries()
    return render_template("journal.html", entries=entries)


if __name__ == "__main__":
    app.run(debug=True)  #starts the Flask web server and automates code changes

