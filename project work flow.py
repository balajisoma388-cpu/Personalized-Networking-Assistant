# ============================================================
# AI Event Topic Generator and Fact Checker System
# Single File Version
# ============================================================

from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

# ============================================================
# In-Memory Databases
# ============================================================

history_db = []
feedback_db = []

# ============================================================
# Data Models (Schemas)
# ============================================================

class EventRequest(BaseModel):
    event: str


class FeedbackRequest(BaseModel):
    event: str
    rating: int
    comments: str


# ============================================================
# Event Analyzer Service
# ============================================================

class EventAnalyzer:

    @staticmethod
    def analyze(event: str):
        words = event.split()

        return {
            "word_count": len(words),
            "keywords": words[:5],
            "character_count": len(event)
        }


# ============================================================
# Topic Generator Service
# ============================================================

class TopicGenerator:

    @staticmethod
    def generate(event: str):
        return f"AI Generated Topic: {event.title()}"


# ============================================================
# Fact Checker Service
# ============================================================

class FactChecker:

    @staticmethod
    def check(text: str):

        # Placeholder logic
        if len(text) < 10:
            status = "Insufficient Information"
        else:
            status = "Pending Verification"

        return {
            "status": status,
            "message": "This is a demo fact-checking service."
        }


# ============================================================
# History Logger Service
# ============================================================

class HistoryLogger:

    @staticmethod
    def add(event, topic):
        history_db.append({
            "event": event,
            "topic": topic
        })

    @staticmethod
    def get():
        return history_db


# ============================================================
# Feedback Logger Service
# ============================================================

class FeedbackLogger:

    @staticmethod
    def add(event, rating, comments):
        feedback_db.append({
            "event": event,
            "rating": rating,
            "comments": comments
        })

    @staticmethod
    def get():
        return feedback_db


# ============================================================
# FastAPI Application
# ============================================================

app = FastAPI(
    title="AI Event Topic Generator System",
    description="Single-file implementation of the project.",
    version="1.0"
)


# ============================================================
# Home Route
# ============================================================

@app.get("/")
def home():
    return {
        "message": "AI Event Topic Generator API Running"
    }


# ============================================================
# Generate Topic Route
# ============================================================

@app.post("/generate")
def generate_topic(request: EventRequest):

    analysis = EventAnalyzer.analyze(request.event)

    topic = TopicGenerator.generate(request.event)

    HistoryLogger.add(
        request.event,
        topic
    )

    return {
        "event": request.event,
        "analysis": analysis,
        "generated_topic": topic
    }


# ============================================================
# Fact Checking Route
# ============================================================

@app.post("/factcheck")
def fact_check(request: EventRequest):

    result = FactChecker.check(request.event)

    return result


# ============================================================
# History Route
# ============================================================

@app.get("/history")
def get_history():

    return {
        "history": HistoryLogger.get()
    }


# ============================================================
# Submit Feedback Route
# ============================================================

@app.post("/feedback")
def submit_feedback(request: FeedbackRequest):

    FeedbackLogger.add(
        request.event,
        request.rating,
        request.comments
    )

    return {
        "message": "Feedback Submitted Successfully"
    }


# ============================================================
# Get Feedback Route
# ============================================================

@app.get("/feedback")
def get_feedback():

    return {
        "feedback_history": FeedbackLogger.get()
    }


# ============================================================
# Main Function
# ============================================================

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8000
    )
```
