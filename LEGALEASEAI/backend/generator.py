class LocalDocumentGenerator:
    model_name = "local-fallback"

    def generate_document(
        self,
        document_type: str,
        parties: str,
        terms: str,
        effective_date: str,
    ) -> tuple[str, bool]:
        content = (
            f"{document_type.upper()}\n\n"
            f"Effective Date: {effective_date}\n\n"
            f"Parties\n{parties}\n\n"
            f"Terms and Conditions\n{terms}\n\n"
            "Review Notice\n"
            "This draft is based on the information provided and is not legal advice. "
            "Have it reviewed by a qualified legal professional before signing."
        )
        return content, False
