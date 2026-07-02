# app/models/schemas.py

from typing import List
from pydantic import BaseModel, Field


class EventInput(BaseModel):
    """
    Request model for event analysis.
    """

    description: str = Field(
        ...,
        min_length=10,
        max_length=1000,
        description="Description of the networking event."
    )


class UserInterests(BaseModel):
    """
    Stores the user's professional interests.
    """

    interests: List[str] = Field(
        ...,
        min_items=1,
        description="List of user interests."
    )


class ConversationRequest(BaseModel):
    """
    Request model for generating conversation topics.
    """

    description: str = Field(
        ...,
        min_length=10,
        max_length=1000
    )

    interests: List[str] = Field(
        ...,
        min_items=1
    )


class ConversationResponse(BaseModel):
    """
    Response returned after generating conversation starters.
    """

    topics: List[str]
    suggestions: List[str]


class FactCheckRequest(BaseModel):
    """
    Request model for fact checking.
    """

    query: str = Field(
        ...,
        min_length=5,
        max_length=500
    )


class FactCheckResponse(BaseModel):
    """
    Response model for fact-checking results.
    """

    summary: str
    verified: bool
    confidence: float = Field(
        ...,
        ge=0.0,
        le=1.0,
        description="Confidence score between 0 and 1."
    )