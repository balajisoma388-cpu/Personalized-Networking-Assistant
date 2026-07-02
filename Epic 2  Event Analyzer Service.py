# app/services/event_analyzer.py

"""
Event Analyzer Service

This service is responsible for extracting the most relevant themes
from a networking event description using Hugging Face's
zero-shot classification pipeline.

The DistilBERT model is loaded once when the module is imported,
improving application performance by avoiding repeated model loading.
"""

from typing import List, Optional

from transformers import pipeline
from app.config import MODEL_NAMES

# Load the model once during application startup
classifier = pipeline(
    task="zero-shot-classification",
    model=MODEL_NAMES["event_analysis"]
)

# Default professional networking themes
DEFAULT_LABELS = [
    "Artificial Intelligence",
    "Machine Learning",
    "Healthcare",
    "Blockchain",
    "Cybersecurity",
    "Cloud Computing",
    "Education",
    "Business",
    "Entrepreneurship",
    "Marketing",
    "Finance",
    "Networking",
    "Innovation",
    "Leadership",
    "Sustainability"
]


def extract_event_themes(
    description: str,
    candidate_labels: Optional[List[str]] = None
) -> List[str]:
    """
    Extract the top three themes from an event description.

    Parameters
    ----------
    description : str
        The networking event description.

    candidate_labels : list[str], optional
        Custom labels to classify against.
        If omitted, the default professional themes are used.

    Returns
    -------
    list[str]
        Top three predicted themes ranked by confidence.
    """

    if not description.strip():
        raise ValueError("Event description cannot be empty.")

    labels = candidate_labels or DEFAULT_LABELS

    result = classifier(
        sequences=description,
        candidate_labels=labels,
        multi_label=True
    )

    return result["labels"][:3]


def extract_event_analysis(
    description: str,
    candidate_labels: Optional[List[str]] = None
) -> dict:
    """
    Return the top three themes along with their confidence scores.

    Returns
    -------
    dict
        {
            "themes": [...],
            "scores": [...]
        }
    """

    labels = candidate_labels or DEFAULT_LABELS

    result = classifier(
        sequences=description,
        candidate_labels=labels,
        multi_label=True
    )

    return {
        "themes": result["labels"][:3],
        "scores": [round(score, 3) for score in result["scores"][:3]]
    }


if __name__ == "__main__":
    sample_description = (
        "Join AI researchers and technology leaders to discuss "
        "the latest innovations in machine learning, cloud computing, "
        "and cybersecurity."
    )

    print("Top Themes:")
    print(extract_event_themes(sample_description))

    print("\nDetailed Analysis:")
    print(extract_event_analysis(sample_description))