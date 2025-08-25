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

