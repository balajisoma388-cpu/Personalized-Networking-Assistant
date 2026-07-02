# frontend/streamlit_app.py

"""
Streamlit Frontend
------------------

This module provides the user interface for the
Personalized Networking Assistant.

Responsibilities
----------------
• Connect to the FastAPI backend
• Collect user input
• Display AI-generated conversation starters
• Submit fact-check requests
• Record user feedback
• View conversation and feedback history
"""

import json
import sys
from pathlib import Path

import requests
import streamlit as st

# ----------------------------------------------------
# Allow Streamlit to import backend modules
# ----------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from app.services import feedback_logger


# ----------------------------------------------------
# Backend Configuration
# ----------------------------------------------------

BASE_URL = "http://127.0.0.1:8000"


# ----------------------------------------------------
# Streamlit Page Configuration
# ----------------------------------------------------

st.set_page_config(
    page_title="Personalized Networking Assistant",
    page_icon="🤝",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("🤝 Personalized Networking Assistant")
st.markdown(
    """
Generate professional networking conversation starters using AI.
The application communicates with a FastAPI backend that performs
event analysis, conversation generation, fact checking, and history logging.
"""
)

# Display backend connection status
try:
    response = requests.get(f"{BASE_URL}/", timeout=3)

    if response.status_code == 200:
        st.success("✅ Connected to FastAPI backend")
    else:
        st.warning("⚠ Backend is running but returned an unexpected response.")

except requests.exceptions.RequestException:
    st.error(
        "❌ Unable to connect to the FastAPI backend.\n\n"
        "Start the backend first using:\n\n"
        "uvicorn app.main:app --reload"
    )