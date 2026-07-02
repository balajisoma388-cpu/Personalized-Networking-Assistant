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

router = APIRouter(tags=["Networking Assistant"])


@router.post(
    "/analyze-event",
    response_model=dict,
    summary="Analyze an event description"
)
def analyze_event(data: EventInput):
    """
    Extract the top three themes from an event description.
    """

    themes = event_analyzer.extract_event_themes(data.description)

    return {
        "topics": themes
    }


@router.post(
    "/fact-check",
    response_model=FactCheckResponse,
    summary="Fact check a topic"
)
def check_fact(data: FactCheckRequest):
    """
    Retrieve a factual summary from Wikipedia.
    """

    summary = fact_checker.fact_check(data.query)

    return FactCheckResponse(summary=summary)


@router.post(
    "/generate-conversation",
    response_model=ConversationResponse,
    summary="Generate networking conversation starters"
)
def generate_conversation(data: ConversationRequest):
    """
    Complete AI conversation generation pipeline.
    """

    themes = event_analyzer.extract_event_themes(
        data.description
    )

    suggestions = topic_generator.generate_topics(
        themes,
        data.interests
    )

    history_logger.log_conversation(
        {
            "description": data.description,
            "interests": data.interests,
            "topics": themes,
            "suggestions": suggestions,
        }
    )

    return ConversationResponse(
        topics=themes,
        suggestions=suggestions,
    )