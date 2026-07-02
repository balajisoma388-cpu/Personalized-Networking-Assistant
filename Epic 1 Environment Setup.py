"""
environment.py

Story 3: Environment Setup

This module verifies that the required Python packages are installed
and displays the current project environment information.
"""

import importlib
import platform
import sys


class EnvironmentChecker:
    """Checks whether all required packages are installed."""

    REQUIRED_PACKAGES = [
        "fastapi",
        "uvicorn",
        "streamlit",
        "transformers",
        "torch",
        "requests",
        "pydantic",
        "pytest",
        "httpx"
    ]

    @staticmethod
    def check_python_version():
        """Display the current Python version."""
        print("=" * 60)
        print("PYTHON ENVIRONMENT")
        print("=" * 60)
        print(f"Python Version : {platform.python_version()}")
        print(f"Platform       : {platform.system()} {platform.release()}")
        print(f"Executable     : {sys.executable}")

    @classmethod
    def verify_packages(cls):
        """Verify that all required packages are installed."""

        print("\nChecking Required Packages\n")

        missing_packages = []

        for package in cls.REQUIRED_PACKAGES:
            try:
                module = importlib.import_module(package)

                version = getattr(module, "__version__", "Unknown")

                print(f"✓ {package:<15} Version: {version}")

            except ImportError:
                print(f"✗ {package:<15} NOT INSTALLED")
                missing_packages.append(package)

        return missing_packages


def print_setup_instructions():
    """Display the environment setup instructions."""

    print("\n" + "=" * 60)
    print("ENVIRONMENT SETUP")
    print("=" * 60)

    print("""
1. Create a virtual environment

   Windows:
       python -m venv venv

   macOS / Linux:
       python3 -m venv venv

2. Activate the virtual environment

   Windows:
       venv\\Scripts\\activate

   macOS / Linux:
       source venv/bin/activate

3. Install dependencies

       pip install -r requirements.txt

4. Verify installation

       python environment.py
""")


def main():
    checker = EnvironmentChecker()

    checker.check_python_version()

    missing = checker.verify_packages()

    if missing:
        print("\nMissing Packages:")
        for package in missing:
            print(f" - {package}")
        print("\nRun:")
        print("pip install -r requirements.txt")
    else:
        print("\nAll required packages are installed.")

    print_setup_instructions()


if __name__ == "__main__":
    main()