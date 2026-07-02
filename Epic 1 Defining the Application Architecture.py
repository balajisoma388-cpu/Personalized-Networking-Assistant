"""
architecture.py

Story 2: Defining the Application Architecture

This module defines the architecture of the AI Networking Assistant.
The application follows a modular three-tier architecture consisting of:

1. Presentation Layer (Streamlit Frontend)
2. API Layer (FastAPI Routers)
3. Service Layer (AI Processing Services)

Benefits
--------
- Separation of Concerns
- Easy Testing
- Extensibility
- Maintainability
"""

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Layer:
    """Represents one architectural layer."""
    name: str
    responsibility: str
    modules: List[str]


class ApplicationArchitecture:
    """
    Describes the modular architecture of the project.
    """

    def __init__(self):
        self.layers = [
            Layer(
                name="Presentation Layer",
                responsibility="Collect user input and display AI-generated results.",
                modules=[
                    "Streamlit UI",
                    "Conversation History",
                    "Feedback View"
                ]
            ),
            Layer(
                name="API Layer",
                responsibility="Expose REST endpoints using FastAPI.",
                modules=[
                    "conversation.py",
                    "API Routing",
                    "Request Validation"
                ]
            ),
            Layer(
                name="Service Layer",
                responsibility="Business logic and AI processing.",
                modules=[
                    "event_analyzer.py",
                    "topic_generator.py",
                    "fact_checker.py",
                    "history_logger.py",
                    "feedback_logger.py"
                ]
            )
        ]

    def display_architecture(self):
        """Print the architecture layers."""

        print("\nAPPLICATION ARCHITECTURE")
        print("=" * 50)

        for layer in self.layers:
            print(f"\n{layer.name}")
            print("-" * len(layer.name))
            print(f"Responsibility: {layer.responsibility}")

            print("Modules:")
            for module in layer.modules:
                print(f"  • {module}")


class DirectoryStructure:
    """
    Represents the project directory organization.
    """

    structure: Dict[str, List[str]] = {
        "app": [
            "main.py",
            "config.py",
            "models/schemas.py",
            "routers/conversation.py",
            "services/event_analyzer.py",
            "services/topic_generator.py",
            "services/fact_checker.py",
            "services/history_logger.py",
            "services/feedback_logger.py"
        ],
        "frontend": [
            "streamlit_app.py"
        ],
        "tests": [
            "conftest.py",
            "test_event_analyzer.py",
            "test_fact_checker.py",
            "test_routes.py"
        ]
    }

    @classmethod
    def display_structure(cls):
        """Display the directory hierarchy."""

        print("\nPROJECT DIRECTORY STRUCTURE")
        print("=" * 50)

        for folder, files in cls.structure.items():
            print(f"\n{folder}/")

            for file in files:
                print(f"   ├── {file}")


class DataFlow:
    """
    Demonstrates how data flows through the application.
    """

    @staticmethod
    def display():

        flow = [
            "User",
            "Streamlit Frontend",
            "FastAPI Router",
            "AI Services",
            "Response",
            "Frontend Display"
        ]

        print("\nAPPLICATION DATA FLOW")
        print("=" * 50)

        print("  ->  ".join(flow))


def main():
    architecture = ApplicationArchitecture()

    architecture.display_architecture()

    DirectoryStructure.display_structure()

    DataFlow.display()


if __name__ == "__main__":
    main()