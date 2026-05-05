import streamlit as st
from utils.chain import get_recommendations

st.set_page_config(page_title="AI Product Assistant", page_icon="🛒")

st.title("🛒 AI Product Recommendation Assistant")
st.write("Find the best products using AI")

# Input
query = st.text_area("What are you looking for? (e.g. best laptop for coding under 150k PKR)")

# Button
if st.button("Get Recommendations"):
    if query:
        with st.spinner("Finding best products..."):
            result = get_recommendations(query)

        st.success("Recommendations Ready!")

        st.markdown("## 🧠 AI Suggestions")
        st.write(result)
    else:
        st.warning("Please enter your requirement")

st.markdown("---")
st.caption("⚠️ AI suggestions only. Always verify before purchasing.")