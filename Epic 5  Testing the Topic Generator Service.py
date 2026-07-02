from app.services import topic_generator


def test_topic_generation_returns_suggestions():
    """The generator should return a non-empty list of suggestions."""

    themes = ["AI", "healthcare"]
    interests = ["ethics", "automation"]

    suggestions = topic_generator.generate_topics(themes, interests)

    assert isinstance(suggestions, list)
    assert len(suggestions) > 0


def test_topic_generation_returns_strings():
    """Every generated suggestion should be a string."""

    themes = ["AI", "healthcare"]
    interests = ["ethics", "automation"]

    suggestions = topic_generator.generate_topics(themes, interests)

    assert all(isinstance(suggestion, str) for suggestion in suggestions)


def test_topic_generation_non_empty_strings():
    """Suggestions should not contain empty or whitespace-only strings."""

    themes = ["AI", "healthcare"]
    interests = ["ethics", "automation"]

    suggestions = topic_generator.generate_topics(themes, interests)

    assert all(suggestion.strip() != "" for suggestion in suggestions)


def test_topic_generation_returns_at_most_three():
    """The generator should return no more than three suggestions."""

    themes = ["AI", "healthcare"]
    interests = ["ethics", "automation"]

    suggestions = topic_generator.generate_topics(themes, interests)

    assert len(suggestions) <= 3