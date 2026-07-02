"""
model_selection.py

Model Selection Module

This module initializes two NLP models:

1. DistilBERT (Zero-Shot Classification)
   - Used for extracting themes from networking event descriptions.

2. GPT-2 Small (Text Generation)
   - Used for generating professional conversation starters.
"""

from transformers import pipeline


class NLPModelManager:
    """
    Loads and manages NLP models for the application.
    """

    def __init__(self):
        self.theme_classifier = None
        self.conversation_generator = None

    def load_models(self):
        """
        Load all required Hugging Face models.
        """
        try:
            print("Loading DistilBERT Zero-Shot Classifier...")

            self.theme_classifier = pipeline(
                task="zero-shot-classification",
                model="typeform/distilbert-base-uncased-mnli"
            )

            print("✓ DistilBERT loaded successfully.")

            print("Loading GPT-2 Small...")

            self.conversation_generator = pipeline(
                task="text-generation",
                model="gpt2"
            )

            print("✓ GPT-2 Small loaded successfully.")

        except Exception as error:
            print(f"Error loading models: {error}")

    def extract_theme(self, event_description: str):
        """
        Classify an event description into the most suitable theme.

        Parameters
        ----------
        event_description : str
            Description of the networking event.

        Returns
        -------
        dict
            Highest-scoring theme and confidence.
        """

        candidate_labels = [
            "Technology",
            "Artificial Intelligence",
            "Business",
            "Entrepreneurship",
            "Marketing",
            "Healthcare",
            "Education",
            "Finance",
            "Networking",
            "Innovation"
        ]

        result = self.theme_classifier(
            event_description,
            candidate_labels
        )

        return {
            "theme": result["labels"][0],
            "confidence": round(result["scores"][0], 3)
        }

    def generate_conversation(self, theme: str):
        """
        Generate a professional conversation starter.

        Parameters
        ----------
        theme : str
            Theme extracted from the event.

        Returns
        -------
        str
            Generated conversation starter.
        """

        prompt = (
            f"You are attending a professional networking event "
            f"focused on {theme}. "
            f"Generate a friendly conversation starter:"
        )

        output = self.conversation_generator(
            prompt,
            max_length=60,
            num_return_sequences=1,
            temperature=0.8,
            do_sample=True,
            pad_token_id=50256
        )

        return output[0]["generated_text"]


def main():
    """
    Example usage of the NLP Model Manager.
    """

    manager = NLPModelManager()

    manager.load_models()

    event = (
        "Join industry leaders to discuss the latest "
        "advancements in Artificial Intelligence "
        "and Machine Learning."
    )

    print("\nEvent Description:")
    print(event)

    print("\nExtracting Theme...")

    theme_result = manager.extract_theme(event)

    print("Detected Theme:", theme_result["theme"])
    print("Confidence:", theme_result["confidence"])

    print("\nGenerating Conversation Starter...\n")

    conversation = manager.generate_conversation(
        theme_result["theme"]
    )

    print(conversation)


if __name__ == "__main__":
    main()