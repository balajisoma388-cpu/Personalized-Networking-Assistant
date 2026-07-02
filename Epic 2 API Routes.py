# app/routers/conversation.py

"""
Conversation Router

This router exposes the application's REST API endpoints.

Endpoints
---------
POST /analyze-event
    Extract themes from an event description.

POST /fact-check
    Retrieve a factual summary from Wikipedia.

POST /generate-conversation
    Generate conversation starters based on an event description
    and user interests. The generated conversation is
    automatically saved to the conversation history.
"""

from fastapi import APIRouter, HTTPException

from app.models.schemas import (
    EventInput,
    ConversationRequest,
    ConversationResponse,
    FactCheckRequest,
    FactCheckResponse,
)

from app.services import (
    event_analyzer,
    topic_generator,
    fact_checker,
    history_logger,
)

router = APIRouter(
    prefix="",
    tags=["Conversation Assistant"]
)


@router.post("/analyze-event")
def analyze_event(data: EventInput):
    """
    Analyze an event description and extract the top themes.
    """

    try:
        themes = event_analyzer.extract_event_themes(data.description)

        return {
            "topics": themes
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.post(
    "/fact-check",
    response_model=FactCheckResponse
)
def check_fact(data: FactCheckRequest):
    """
    Retrieve a factual summary from Wikipedia.
    """

    try:
        summary = fact_checker.fact_check(data.query)

        return FactCheckResponse(
            summary=summary,
            verified=True,
            confidence=1.0
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.post(
    "/generate-conversation",
    response_model=ConversationResponse
)
def generate_conversation(data: ConversationRequest):
    """
    Complete conversation generation pipeline.

    Workflow
    --------
    1. Analyze event description.
    2. Extract event themes.
    3. Generate conversation starters.
    4. Save conversation to history.
    5. Return topics and suggestions.
    """

    try:

        # Step 1: Extract event themes
        themes = event_analyzer.extract_event_themes(
            data.description
        )

        # Step 2: Generate conversation starters
        suggestions = topic_generator.generate_topics(
            themes,
            data.interests
        )

        # Step 3: Automatically save conversation
        history_logger.log_conversation(
            {
                "description": data.description,
                "interests": data.interests,
                "topics": themes,
                "suggestions": suggestions
            }
        )

        # Step 4: Return response
        return ConversationResponse(
            topics=themes,
            suggestions=suggestions
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )