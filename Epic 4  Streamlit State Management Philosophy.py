import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

# Initialize session state variables
if "topics" not in st.session_state:
    st.session_state["topics"] = []

if "suggestions" not in st.session_state:
    st.session_state["suggestions"] = []

# User inputs
event_description = st.text_area("📝 Enter Event Description")
user_interests = st.text_input("🎯 Your Interests (comma-separated)")

# Generate conversation starters
if st.button("Generate Conversation Starters"):
    if event_description and user_interests:

        payload = {
            "description": event_description,
            "interests": [
                interest.strip()
                for interest in user_interests.split(",")
            ]
        }

        response = requests.post(
            f"{BASE_URL}/generate-conversation",
            json=payload
        )

        if response.status_code == 200:
            data = response.json()

            # Persist data across Streamlit reruns
            st.session_state["topics"] = data["topics"]
            st.session_state["suggestions"] = data["suggestions"]

        else:
            st.error("Failed to generate conversation starters.")

# Display stored results after every rerun
if st.session_state["suggestions"]:

    st.subheader("🧠 Extracted Topics")
    st.write(st.session_state["topics"])

    st.subheader("💬 Conversation Starters")
    for suggestion in st.session_state["suggestions"]:
        st.markdown(f"- {suggestion}")