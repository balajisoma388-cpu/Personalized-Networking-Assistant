# app/main.py

"""
Personalized Networking Assistant

Application Entry Point

Architecture
------------
This application follows a hub-and-spoke routing architecture.

                  main.py
                     │
          ───────────┼───────────
                     │
      conversation.py (Router)
                     │
     ┌───────────────┼────────────────┐
     │               │                │
 Event Analyzer  Topic Generator  Fact Checker
     │               │                │
     └───────────────┼────────────────┘
                     │
        History Logger / Feedback Logger
                     │
                 JSON Storage

Responsibilities
----------------
• Create the FastAPI application
• Register all routers
• Provide health-check endpoints
• Delegate business logic to routers
"""

from fastapi import FastAPI
from app.routers.conversation import router as conversation_router

app = FastAPI(
    title="Personalized Networking Assistant",
    description="AI-powered networking assistant using DistilBERT and GPT-2",
    version="1.0.0"
)

# Register all routers
app.include_router(conversation_router)


@app.get("/", tags=["Health"])
def root():
    """
    Root endpoint used for health checks.
    """

    return {
        "status": "healthy",
        "message": "Personalized Networking Assistant API is running."
    }


@app.get("/health", tags=["Health"])
def health():
    """
    Monitoring endpoint.
    """

    return {
        "status": "UP"
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )