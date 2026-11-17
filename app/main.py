"""Minimal FastAPI service with a root route, a health route, and a CPU-burn
route used later to demonstrate HPA."""

import os
import time

from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI(
    title="Hello API",
    version=os.getenv("APP_VERSION", "dev"),
)


@app.get("/")
def root() -> dict[str, str]:
    """Business endpoint. Returns JSON."""
    return {"message": "Hello from API"}


@app.get("/health", response_class=PlainTextResponse)
def health() -> str:
    """Liveness/readiness endpoint. Cheap, no dependencies, plain text."""
    return "OK"


@app.get("/burn", response_class=PlainTextResponse)
def burn(ms: int = 200) -> str:
    """Burn CPU for ~`ms` milliseconds. Used to drive HPA load tests (Section 18).
    Never ship an endpoint like this to prod — it exists purely to create load."""
    end = time.time() + ms / 1000.0
    x = 0
    while time.time() < end:
        x += 1
    return f"burned {ms}ms"

