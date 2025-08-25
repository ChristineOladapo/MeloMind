import json

JOURNAL_FILE = "journal.json"


def load_all_entries():
    try:
        with open(JOURNAL_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def load_entries(username):
    """Read and return the list of entries from journal.json."""
    all_entries = load_all_entries()
    return all_entries.get(username, [])

def save_entry(username, entry_text):
    """Insert a new entry at the top of journal.json."""
    all_entries = load_all_entries()
    if username not in all_entries:
        all_entries[username] = []
    all_entries[username].append({"entry": entry_text})
    with open(JOURNAL_FILE, "w") as f:
        json.dump(all_entries, f, indent=4)