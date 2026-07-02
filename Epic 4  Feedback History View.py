# --- FEEDBACK HISTORY ---

st.markdown("---")
st.subheader("🗂 View Feedback History")

feedback_path = Path("feedback.json")

if st.button("Show Feedback"):

    if feedback_path.exists():

        with open(feedback_path, "r") as f:
            feedback_data = json.load(f)

        # Display latest 10 feedback entries (newest first)
        for item in reversed(feedback_data[-10:]):

            icon = "👍" if item["feedback"] == "like" else "👎"

            st.markdown(f"{icon} **{item['suggestion']}**")
            st.caption(f"🕒 {item['timestamp']}")
            st.markdown("---")

    else:
        st.info("No feedback submitted yet.")