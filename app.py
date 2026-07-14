import streamlit as st

from src.retriever import DocumentRetriever

st.set_page_config(
    page_title="Enterprise Knowledge Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Enterprise Knowledge Assistant")
st.markdown("---")

st.write("Ask questions from company policy documents.")

query = st.text_input(
    "Enter your question:",
    placeholder="Example: What is the medical insurance coverage?"
)

if st.button("Search"):

    if query.strip() == "":
        st.warning("Please enter a question.")
        st.stop()

    with st.spinner("Searching documents..."):

        retriever = DocumentRetriever()

        results = retriever.search(query)

    st.success(f"{len(results)} relevant document(s) found.")

    st.markdown("---")

    for i, result in enumerate(results, start=1):

        with st.expander(f"Result {i}"):

            st.write(f"**Source:** {result.metadata.get('source')}")

            st.write(result.page_content)