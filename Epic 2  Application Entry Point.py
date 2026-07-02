# app/main.py

"""
Application Entry Point

This module creates the FastAPI application instance,
registers all API routers, and exposes a simple health-check
endpoint.

Responsibilities
---------------
1. Create the FastAPI application.
2. Register routers.
3. Expose a root endpoint for health monitoring.
"""

from fastapi import FastAPI

from app.routers.conversation import router as conversation_router


app = FastAPI(
    title="Personalized Networking Assistant",
    description="AI-powered networking assistant using DistilBERT and GPT-2",
    version="1.0.0"
)

# Register API routes
app.include_router(conversation_router)


@app.get("/")
def root():
    """
    Health-check endpoint.

    Returns
    -------
    dict
        Simple status message indicating the API is running.
    """
    return {
        "status": "healthy",
        "message": "Welcome to the Personalized Networking Assistant API"
    }


@app.get("/health")
def health_check():
    """
    Dedicated health endpoint for monitoring systems.

    Returns
    -------
    dict
        Service health information.
    """
    return {
        "status": "up"
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )