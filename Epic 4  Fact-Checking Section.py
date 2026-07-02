# ----------------------------------------------------
# FACT CHECK SECTION
# ----------------------------------------------------

st.divider()

st.header("🔍 Quick Fact Check")

fact_query = st.text_input(
    "Enter a topic to fact-check",
    placeholder="Example: Artificial Intelligence"
)

if st.button("Fact Check"):

    if fact_query.strip():

        try:

            response = requests.post(
                f"{BASE_URL}/fact-check",
                json={"query": fact_query},
                timeout=30
            )

            if response.status_code == 200:

                result = response.json()

                st.success(result["summary"])

            else:

                st.error("Fact-checking failed.")

        except requests.exceptions.RequestException as e:

            st.error(f"Unable to connect to the backend: {e}")

    else:

        st.warning("Please enter a topic to fact-check.")