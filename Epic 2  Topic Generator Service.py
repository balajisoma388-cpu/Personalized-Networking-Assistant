# app/services/topic_generator.py

"""
Topic Generator Service

This service generates professional networking conversation starters
using the GPT-2 Small language model.

The GPT-2 model is loaded once during application startup for improved
performance. A fixed random seed is used to ensure reproducible outputs
during testing and debugging.
"""

from typing import List

from transformers import pipeline, set_seed

from app.config import MODEL_NAMES

# Load GPT-2 once at application startup
generator = pipeline(
    task="text-generation",
    model=MODEL_NAMES["conversation_generation"]
)

# Ensure reproducible outputs
set_seed(42)


def generate_topics(
    event_themes: List[str],
    user_interests: List[str]
) -> List[str]:
    """
    Generate conversation starters based on event themes
    and user interests.

    Parameters
    ----------
    event_themes : List[str]
        Themes extracted from the event description.

    user_interests : List[str]
        Professional interests provided by the user.

    Returns
    -------
    List[str]
        A list containing up to three conversation starters.
    """

    if not event_themes:
        raise ValueError("At least one event theme is required.")

    if not user_interests:
        raise ValueError("At least one user interest is required.")

    prompt = (
        f"I'm attending a professional networking event focused on "
        f"{', '.join(event_themes)}. "
        f"My interests include {', '.join(user_interests)}. "
        f"Generate three short, engaging conversation starters:\n"
    )

    outputs = generator(
        prompt,
        max_length=80,
        num_return_sequences=1,
        do_sample=True,
        temperature=0.8,
        top_p=0.95,
        pad_token_id=50256
    )

    generated_text = outputs[0]["generated_text"]

    # Remove the original prompt from the generated output
    generated_text = generated_text.replace(prompt, "").strip()

    # Split into lines and clean formatting
    suggestions = []

    for line in generated_text.split("\n"):
        line = line.strip()

        if not line:
            continue

        line = line.lstrip("-•1234567890. ").strip()

        if len(line) > 5:
            suggestions.append(line)

        if len(suggestions) == 3:
            break

    # Fallback if GPT-2 does not generate newline-separated items
    if not suggestions:
        suggestions = [
            "What inspired you to attend this event?",
            "Which emerging trend in this field excites you the most?",
            "What projects are you currently working on?"
        ]

    return suggestions


if __name__ == "__main__":

    themes = [
        "Artificial Intelligence",
        "Machine Learning",
        "Innovation"
    ]

    interests = [
        "Data Science",
        "Python",
        "Cloud Computing"
    ]

    print("Generated Conversation Starters:\n")

    for index, topic in enumerate(
        generate_topics(themes, interests),
        start=1
    ):
        print(f"{index}. {topic}")