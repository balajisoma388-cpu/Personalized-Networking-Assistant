# ----------------------------------------------------
# INPUT SECTION
# ----------------------------------------------------

st.header("Generate Conversation Starters")

event_description = st.text_area(
    "📝 Enter Event Description",
    placeholder="Example: AI and Machine Learning Conference focusing on healthcare innovation."
)

user_interests = st.text_input(
    "🎯 Your Interests (comma-separated)",
    placeholder="AI, Machine Learning, Healthcare"
)

if st.button("Generate Conversation Starters"):

    if event_description.strip() and user_interests.strip():

        payload = {
            "description": event_description,
            "interests": [
                interest.strip()
                for interest in user_interests.split(",")
                if interest.strip()
            ]
        }

        try:

            response = requests.post(
                f"{BASE_URL}/generate-conversation",
                json=payload,
                timeout=60
            )

            if response.status_code == 200:

                data = response.json()

                # Persist results across Streamlit reruns
                st.session_state["topics"] = data["topics"]
                st.session_state["suggestions"] = data["suggestions"]

                st.success("Conversation starters generated successfully!")

            else:
                st.error(
                    f"Backend Error ({response.status_code})"
                )

        except requests.exceptions.RequestException as e:

            st.error(f"Connection failed: {e}")

    else:

        st.warning(
            "Please enter both the event description and your interests."
        )