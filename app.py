from flask import Flask, render_template, request, jsonify
from backend.journal import load_entries, save_entry

#name tells flask to use this as the main application

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  #loads HTML file 

@app.route("/chatbot")  #chatbot route
def chatbot():
    return "This is the chatbot page!"


@app.route("/journal", methods=["GET", "POST"])
def journal():
    if request.method == "POST":
        data = request.get_json()
        entry = data.get("entry", "").strip()
        if not entry:
            return jsonify({"error": "Entry cannot be empty"}), 400
        save_entry(entry)
        return jsonify({"message": "Journal entry saved!"})
    # GET
    entries = load_entries()
    return render_template("journal.html", entries=entries)


if __name__ == "__main__":  # only runs Flask if script is executed directly
    app.run(debug=True)  #starts the Flask web server and automates code changes

