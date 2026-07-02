# app/services/base_service.py

"""
Service Layer Design Principles

This module illustrates the architectural principles followed
by all services in the Personalized Networking Assistant.

Principles
----------
1. Single Responsibility Principle (SRP)
2. Dependency Injection via Imports
3. Stateless Service Functions
"""

from abc import ABC, abstractmethod
from typing import Any


class BaseService(ABC):
    """
    Abstract base class for all application services.
    """

    @abstractmethod
    def execute(self, *args, **kwargs) -> Any:
        """
        Execute the service.

        Each concrete service implements its own business logic.
        """
        pass


class ExampleService(BaseService):
    """
    Demonstrates a stateless service implementation.
    """

    def execute(self, text: str) -> str:
        if not text.strip():
            raise ValueError("Input cannot be empty.")

        return text.upper()


if __name__ == "__main__":

    service = ExampleService()

    print(service.execute("Artificial Intelligence"))