from fastapi import APIRouter, HTTPException

from .generator import LocalDocumentGenerator

from .schemes import (
    DocumentRequest,
    DocumentResponse
)


router = APIRouter()

generator = LocalDocumentGenerator()


@router.post(
    "/generate",
    response_model=DocumentResponse
)
def generate_document(
    request: DocumentRequest
):

    try:

        content, ai_generated = (
            generator.generate_document(
                document_type=request.document_type,
                parties=request.parties,
                terms=request.terms,
                effective_date=request.effective_date,
            )
        )

        return DocumentResponse(
            document_type=request.document_type,
            content=content,
            ai_generated=ai_generated,
            model=(
                generator.model_name
                if ai_generated
                else "local-fallback"
            ),
        )

    except Exception as exc:

        raise HTTPException(
            status_code=500,
            detail=(
                f"Document generation failed: {exc}"
            )
        ) from exc