from app.services import event_analyzer


def test_event_analysis_returns_labels():
    """The function should return a non-empty list."""
    result = event_analyzer.extract_event_themes(
        "AI in healthcare and diagnostics"
    )

    assert isinstance(result, list)
    assert len(result) > 0


def test_event_analysis_returns_max_three_labels():
    """The function should return at most three themes."""
    result = event_analyzer.extract_event_themes(
        "AI in healthcare and diagnostics"
    )

    assert len(result) <= 3


def test_event_analysis_labels_are_valid():
    """Returned labels should come from the candidate label set."""

    candidate_labels = [
        "AI",
        "healthcare",
        "blockchain",
        "education",
        "sustainability",
    ]

    result = event_analyzer.extract_event_themes(
        "AI in healthcare and diagnostics",
        candidate_labels=candidate_labels,
    )

    assert all(label in candidate_labels for label in result)


def test_event_analysis_custom_candidate_labels():
    """Custom candidate labels should be supported."""

    labels = ["Python", "Java", "Cloud"]

    result = event_analyzer.extract_event_themes(
        "Python developers conference",
        candidate_labels=labels,
    )

    assert isinstance(result, list)
    assert len(result) <= 3
    assert all(label in labels for label in result)