"""Tests for the manifold module."""

from vid.core.manifold import project, transform


def test_transform() -> None:
    """Test transform function."""
    result = transform()
    assert result is None


def test_project() -> None:
    """Test project function."""
    result = project()
    assert result is None
