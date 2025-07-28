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
    """Append a new entry to journal.json."""
    entries = load_entries()
    entries.append({"entry": entry_text})
    with open(JOURNAL_FILE, "w") as f:
        json.dump(entries, f, indent=4)