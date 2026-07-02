def project_info():
    print("=" * 70)
    print("🤝 Personalized Networking Assistant")
    print("=" * 70)

    print("\nProject Overview")
    print("----------------")
    print("An AI-powered networking assistant that helps users:")
    print("- Generate personalized conversation starters")
    print("- Perform quick fact-checking")
    print("- Store conversation history")
    print("- Collect user feedback")

    print("\nFeatures")
    print("--------")
    features = [
        "AI-based event theme extraction using DistilBERT",
        "Conversation starter generation using GPT-2",
        "Wikipedia fact-checking",
        "Conversation history logging",
        "Feedback collection",
        "FastAPI backend",
        "Streamlit frontend",
        "Swagger API documentation",
        "Pytest unit and integration testing"
    ]

    for feature in features:
        print(f"• {feature}")

    print("\nTech Stack")
    print("----------")
    print("Backend  : FastAPI, Python")
    print("Frontend : Streamlit")
    print("Models   : DistilBERT, GPT-2")
    print("Testing  : pytest, FastAPI TestClient")

    print("\nAPI Endpoints")
    print("-------------")
    endpoints = [
        ("POST", "/analyze-event", "Extract event themes"),
        ("POST", "/generate-conversation", "Generate conversation starters"),
        ("POST", "/fact-check", "Fact-check using Wikipedia"),
        ("GET", "/", "Health Check")
    ]

    for method, endpoint, description in endpoints:
        print(f"{method:<6} {endpoint:<25} {description}")

    print("\nHow to Run")
    print("----------")
    print("1. Start FastAPI Backend:")
    print("   uvicorn app.main:app --reload")

    print("\n2. Start Streamlit Frontend:")
    print("   streamlit run frontend/streamlit_app.py")

    print("\nBackend URL")
    print("-----------")
    print("http://127.0.0.1:8000")

    print("\nSwagger UI")
    print("----------")
    print("http://127.0.0.1:8000/docs")

    print("\nFrontend")
    print("--------")
    print("http://localhost:8501")

    print("\nTesting")
    print("-------")
    print("Run all tests:")
    print("pytest")

    print("\nRun with coverage:")
    print("pytest --cov=app")

    print("\nFuture Improvements")
    print("-------------------")
    improvements = [
        "User authentication",
        "Database integration",
        "Cloud deployment",
        "Docker support",
        "Recommendation engine",
        "GitHub Actions CI/CD"
    ]

    for item in improvements:
        print(f"• {item}")

    print("\nAuthor")
    print("------")
    print("Your Name")
    print("Personalized Networking Assistant")


if __name__ == "__main__":
    project_info()