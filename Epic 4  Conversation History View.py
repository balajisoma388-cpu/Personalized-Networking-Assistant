# --- CONVERSATION HISTORY ---

st.markdown("---")
st.subheader("📜 View Previous Conversations")

if st.button("Show History"):
    history_path = Path("history.json")

    if history_path.exists():
        with open(history_path, "r") as f:
            history = json.load(f)

        # Display latest 5 conversations (newest first)
        for item in reversed(history[-5:]):
            st.markdown(f"### 🗓 {item['timestamp']}")
            st.write("**Event Description:**", item["description"])
            st.write("**User Interests:**", ", ".join(item["interests"]))
            st.write("**Extracted Topics:**", ", ".join(item["topics"]))

            st.write("**Conversation Starters:**")
            for suggestion in item["suggestions"]:
                st.markdown(f"- {suggestion}")

            st.markdown("---")

    else:
        st.info("No conversation history found.")