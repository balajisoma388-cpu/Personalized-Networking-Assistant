# app/services/feedback_logger.py

"""
Feedback Logger Service

This service records user feedback on generated conversation
suggestions. Each feedback entry is stored in a JSON file
along with a timestamp for future analysis.

The stored feedback can later be used to improve prompt
engineering or recommendation quality.
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List

# Location of the feedback file
FEEDBACK_FILE = Path("feedback.json")


def log_feedback(suggestion: str, action: str) -> None:
    """
    Save user feedback.

    Parameters
    ----------
    suggestion : str
        The generated conversation suggestion.

    action : str
        User feedback ("like" or "dislike").

    Returns
    -------
    None
    """

    if action.lower() not in {"like", "dislike"}:
        raise ValueError("Action must be either 'like' or 'dislike'.")

    entry = {
        "suggestion": suggestion,
        "feedback": action.lower(),
        "timestamp": datetime.now().isoformat()
    }

    # Load existing feedback
    if FEEDBACK_FILE.exists():
        try:
            with FEEDBACK_FILE.open("r", encoding="utf-8") as file:
                feedback = json.load(file)
        except (json.JSONDecodeError, OSError):
            feedback = []
    else:
        feedback = []

    # Add the new entry
    feedback.append(entry)

    # Save updated feedback
    with FEEDBACK_FILE.open("w", encoding="utf-8") as file:
        json.dump(feedback, file, indent=4, ensure_ascii=False)


def get_feedback() -> List[Dict]:
    """
    Retrieve all stored feedback.

    Returns
    -------
    List[Dict]
        List containing all feedback entries.
    """

    if not FEEDBACK_FILE.exists():
        return []

    try:
        with FEEDBACK_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


def clear_feedback() -> None:
    """
    Remove all stored feedback.
    """

    with FEEDBACK_FILE.open("w", encoding="utf-8") as file:
        json.dump([], file, indent=4)


if __name__ == "__main__":

    # Example usage
    log_feedback(
        suggestion="What inspired you to attend this event?",
        action="like"
    )

    log_feedback(
        suggestion="Which AI trend excites you the most?",
        action="dislike"
    )

    print("Current Feedback:\n")

    for item in get_feedback():
        print(item)