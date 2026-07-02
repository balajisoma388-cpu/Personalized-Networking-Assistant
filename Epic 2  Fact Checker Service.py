# app/services/fact_checker.py

"""
Fact Checker Service

This service verifies facts by retrieving a summary from the
Wikipedia REST API.

It provides a simple and reliable way to obtain factual information
without requiring API keys or authentication.
"""

from urllib.parse import quote

import requests

from app.config import FACT_CHECK_API


def fact_check(query: str) -> str:
    """
    Retrieve a factual summary for the given query.

    Parameters
    ----------
    query : str
        The topic or statement to verify.

    Returns
    -------
    str
        A summary extracted from Wikipedia or a user-friendly
        error message if the request fails.
    """

    if not query.strip():
        return "Please provide a valid query."

    try:
        # Encode the query for use in a URL
        encoded_query = quote(query.strip())

        url = f"{FACT_CHECK_API}/{encoded_query}"

        response = requests.get(url, timeout=10)

        response.raise_for_status()

        data = response.json()

        return data.get(
            "extract",
            "No summary found for the requested topic."
        )

    except requests.exceptions.HTTPError:
        return "No matching article was found on Wikipedia."

    except requests.exceptions.Timeout:
        return "The request timed out. Please try again."

    except requests.exceptions.ConnectionError:
        return "Unable to connect to the fact-checking service."

    except requests.exceptions.RequestException:
        return "An unexpected error occurred while retrieving information."

    except ValueError:
        return "Received an invalid response from the fact-checking service."


if __name__ == "__main__":

    topic = "Artificial Intelligence"

    print("Fact Check Result:\n")

    print(fact_check(topic))