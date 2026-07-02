# app/services/history_logger.py

"""
History Logger Service

This service provides persistent storage for generated conversations.
Conversation history is stored in a JSON file using a simple
append-to-list approach.

Each conversation is automatically timestamped to allow users
to revisit previous interactions.
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List

# History file location
HISTORY_FILE = Path("history.json")


def log_conversation(data: Dict) -> None:
    """
    Save a conversation to the history file.

    Parameters
    ----------
    data : dict
        Conversation data to store.

    Returns
    -------
    None
    """

    # Create a copy so the original dictionary isn't modified
    conversation = data.copy()

    # Add timestamp
    conversation["timestamp"] = datetime.now().isoformat()

    # Load existing history
    if HISTORY_FILE.exists():
        try:
            with HISTORY_FILE.open("r", encoding="utf-8") as file:
                history = json.load(file)
        except (json.JSONDecodeError, OSError):
            history = []
    else:
        history = []

    # Append new conversation
    history.append(conversation)

    # Save updated history
    with HISTORY_FILE.open("w", encoding="utf-8") as file:
        json.dump(history, file, indent=4, ensure_ascii=False)


def load_history() -> List[Dict]:
    """
    Load all saved conversations.

    Returns
    -------
    list
        List of conversation records.
    """

    if not HISTORY_FILE.exists():
        return []

    try:
        with HISTORY_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


def clear_history() -> None:
    """
    Delete all stored conversation history.
    """

    with HISTORY_FILE.open("w", encoding="utf-8") as file:
        json.dump([], file, indent=4)


if __name__ == "__main__":

    sample_conversation = {
        "event": "AI Networking Summit",
        "themes": [
            "Artificial Intelligence",
            "Machine Learning",
            "Innovation"
        ],
        "interests": [
            "Python",
            "Data Science"
        ],
        "conversation_starters": [
            "What inspired you to attend this event?",
            "Which AI trend excites you the most?",
            "What projects are you currently working on?"
        ]
    }

    log_conversation(sample_conversation)

    print("Conversation successfully saved.\n")

    print("Conversation History:\n")

    for conversation in load_history():
        print(conversation)