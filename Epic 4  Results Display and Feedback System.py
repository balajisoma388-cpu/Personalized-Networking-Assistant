# ----------------------------------------------------
# DISPLAY RESULTS AND FEEDBACK
# ----------------------------------------------------

if "suggestions" in st.session_state:

    st.header("Results")

    # Display extracted topics
    st.subheader("🧠 Extracted Topics")
    st.write(st.session_state["topics"])

    st.divider()

    # Display conversation starters
    st.subheader("💬 Conversation Starters")

    for i, suggestion in enumerate(st.session_state["suggestions"], start=1):

        st.markdown(f"**{i}.** {suggestion}")

        like_col, dislike_col = st.columns(2)

        with like_col:
            if st.button("👍 Like", key=f"like_{i}"):

                feedback_logger.log_feedback(
                    suggestion=suggestion,
                    action="like"
                )

                st.success("Thank you for your feedback!")

        with dislike_col:
            if st.button("👎 Dislike", key=f"dislike_{i}"):

                feedback_logger.log_feedback(
                    suggestion=suggestion,
                    action="dislike"
                )

                st.info("Feedback recorded.")

        st.divider()