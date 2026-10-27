"""Minimal FastAPI app. Replace with your real application.

Kept in the template so the example test and the CI pipeline work out of the box.
"""

from fastapi import FastAPI

app = FastAPI(title="Project Name")


@app.get("/health")
def health() -> dict[str, str]:
    """Liveness probe. Spec: docs/specs/001-health-check.md"""
    return {"status": "ok"}
