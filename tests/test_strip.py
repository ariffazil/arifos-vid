"""Tests for the strip module."""

from vid.core.strip import extract, filter_strip


def test_extract() -> None:
    """Test extract function."""
    result = extract()
    assert result is None


def test_filter_strip() -> None:
    """Test filter_strip function."""
    result = filter_strip()
    assert result is None
