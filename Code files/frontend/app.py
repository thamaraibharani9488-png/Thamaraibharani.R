import requests
import streamlit as st

st.set_page_config(
    page_title="LegalEase AI",
    page_icon="⚖️",
    layout="centered"
)

st.title("⚖️ LegalEase AI")
st.subheader("Legal Document Generator")

document_type = st.selectbox(
    "Document Type",
    [
        "Rental Agreement",
        "Employment Agreement",
        "NDA",
        "Service Agreement"
    ]
)

parties = st.text_area(
    "Parties",
    placeholder="Example: Landlord: Ravi, Tenant: Kumar"
)

terms = st.text_area(
    "Terms and Conditions",
    placeholder="Enter the main terms..."
)

effective_date = st.date_input("Effective Date")

if st.button("Generate Document"):

    if not parties or not terms:
        st.warning("Please enter Parties and Terms.")
    else:
        data = {
            "document_type": document_type,
            "parties": parties,
            "terms": terms,
            "effective_date": str(effective_date)
        }

        try:
            response = requests.post(
                "http://127.0.0.1:8000/generate",
                json=data
            )

            if response.status_code == 200:
                result = response.json()

                st.success("Document generated successfully! ✅")

                st.text_area(
                    "Generated Document",
                    result.get("content", ""),
                    height=400
                )

            else:
                st.error(
                    f"Backend Error: {response.status_code}"
                )

        except requests.exceptions.ConnectionError:
            st.error(
                "Backend is not running. "
                "Please start FastAPI first."
            )