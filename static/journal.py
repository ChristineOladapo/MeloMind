import json
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

JOURNAL_FILE = "journal.json"

def load_entries():
    """Load journal entries from the JSON file."""
    try:
        with open(JOURNAL_FILE, "r") as file:
            return json.load(file)  # Load existing entries
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # return empty list if file doesn't exist

# only allow get requests/can't add new entries
@app.route("/journal", methods=["GET"])
def show_entries():
    """Show the journal entries on a webpage."""
    entries = load_entries()
    return render_template("journal.html", entries=entries)  #send entries to HTML

@app.route("/journal", methods=["POST"])
def add_entry():
    """Save a new journal entry."""
    data = request.json
    entry = data.get("entry")

    if not entry:
        return jsonify({"error": "Entry cannot be empty"}), 400

    entries = load_entries()
    entries.append({"entry": entry})  # add new entry

    with open(JOURNAL_FILE, "w") as file:
        json.dump(entries, file, indent=4)

    return jsonify({"message": "Journal entry saved!"})

if __name__ == "__main__":
    app.run(debug=True)