"""
Example: Query the Vetted Legal AI Engine

Demonstrates how to send a legal question to the RAG engine,
receive a verified answer with citations, and inspect the
confidence score and validation results.

Prerequisites:
    pip install httpx
    # Ensure the API server is running:
    uvicorn src.vetted_legal_ai.api.routes:app --reload
"""

import httpx
import json
import sys


API_BASE = "http://localhost:8000"


def query_legal_ai(
    question: str,
    jurisdiction: str = "MO",
    max_sources: int = 5,
) -> dict:
    """
    Send a legal question to the Vetted Legal AI engine.

    Args:
        question: The legal question in plain language.
        jurisdiction: Two-letter state code or 'FEDERAL'.
        max_sources: Maximum number of source documents to retrieve.

    Returns:
        The full response dict including answer, citations, and confidence.
    """
    response = httpx.post(
        f"{API_BASE}/query",
        json={
            "question": question,
            "jurisdiction": jurisdiction,
            "max_sources": max_sources,
        },
        timeout=60.0,
    )
    response.raise_for_status()
    return response.json()


def print_result(result: dict) -> None:
    """Pretty-print a query result."""
    print("=" * 72)
    print("ANSWER:")
    print(result["answer"])
    print()
    print(f"Confidence: {result['confidence']}")
    print(f"Audit ID:   {result.get('audit_id', 'N/A')}")
    print()

    citations = result.get("citations", [])
    if citations:
        print(f"CITATIONS ({len(citations)}):")
        for i, cite in enumerate(citations, 1):
            status = cite.get("status", "unknown").upper()
            case_name = cite.get("case_name", "Unknown")
            citation_str = cite.get("citation", "")
            print(f"  {i}. [{status}] {case_name}")
            if citation_str:
                print(f"     {citation_str}")
    else:
        print("No citations returned.")

    print("=" * 72)


def main():
    """Run example queries against the Vetted Legal AI engine."""

    # Example 1: Eviction law question
    print("\n--- Query 1: Eviction Grounds ---\n")
    try:
        result = query_legal_ai(
            question="What are the legal grounds for eviction in Missouri?",
            jurisdiction="MO",
        )
        print_result(result)
    except httpx.ConnectError:
        print(
            "ERROR: Could not connect to the API server.\n"
            "Make sure it is running: uvicorn src.vetted_legal_ai.api.routes:app --reload",
            file=sys.stderr,
        )
        sys.exit(1)

    # Example 2: Federal question with more sources
    print("\n--- Query 2: Federal Fair Housing ---\n")
    result = query_legal_ai(
        question="What protections does the Fair Housing Act provide against disability discrimination?",
        jurisdiction="FEDERAL",
        max_sources=10,
    )
    print_result(result)

    # Example 3: Inspect raw JSON for integration use
    print("\n--- Query 3: Raw JSON Output ---\n")
    result = query_legal_ai(
        question="What is the statute of limitations for personal injury in California?",
        jurisdiction="CA",
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
