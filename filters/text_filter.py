# filters/text_filter.py
import re
from config import BLOCKLIST_FILE

def load_blocklist():
    with open(BLOCKLIST_FILE, "r") as f:
        return [line.strip().lower() for line in f.readlines()]

def contains_blocked_text(text):
    blocklist = load_blocklist()
    for word in blocklist:
        if re.search(rf"\\b{word}\\b", text, re.IGNORECASE):
            return True
    return False
