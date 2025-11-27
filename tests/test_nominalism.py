"""Tests for the nominalism module."""

from vid.core.nominalism import map_concepts, process_nominal


def test_process_nominal() -> None:
    """Test process_nominal function."""
    result = process_nominal()
    assert result is None


def test_map_concepts() -> None:
    """Test map_concepts function."""
    result = map_concepts()
    assert result is None
