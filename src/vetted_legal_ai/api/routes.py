"""
API Routes

FastAPI endpoints for the Vetted Legal AI Engine.
Provides query, audit retrieval, and health check endpoints.
"""

from fastapi import FastAPI

app = FastAPI(
    title="Vetted Legal AI Engine",
    description="RAG engine with citation validation for legal AI",
    version="0.1.0",
)


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "ok"}


# TODO: POST /query — accept a legal question, return validated response
# TODO: GET  /audit/{query_id} — retrieve audit trail for a query
# TODO: GET  /sources — list available legal corpus sources
# TODO: POST /ingest — ingest new legal documents into the corpus
