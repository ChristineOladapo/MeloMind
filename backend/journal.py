import json

JOURNAL_FILE = "journal.json"

def load_entries():
    """Read and return the list of entries from journal.json."""
    try:
        with open(JOURNAL_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_entry(entry_text):
    """Insert a new entry at the top of journal.json."""
    entries = load_entries()
    # entries.append({"entry": entry_text})
    entries.insert(0, {"entry": entry_text})  # append to top
    with open(JOURNAL_FILE, "w") as f:
        json.dump(entries, f, indent=4)