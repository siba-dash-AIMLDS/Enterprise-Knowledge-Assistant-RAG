import streamlit as st

st.set_page_config(
    page_title="Enterprise Knowledge Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Enterprise Knowledge Assistant")

st.markdown("---")

st.write(
    """
    Welcome to the Enterprise Knowledge Assistant.

    Features:
    - Upload enterprise documents
    - Intelligent document search
    - Retrieval-Augmented Generation (RAG)
    - Source citations
    - Enterprise-ready architecture
    """
)

st.sidebar.header("Navigation")

option = st.sidebar.selectbox(
    "Select",
    [
        "Home",
        "Upload Documents",
        "Ask Questions",
        "Settings"
    ]
)

st.success("Sprint 1 Completed Successfully.")