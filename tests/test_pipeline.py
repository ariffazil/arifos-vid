"""Tests for the VID pipeline integration."""

from vid.api.run import execute, main, run_pipeline


def test_run_pipeline() -> None:
    """Test run_pipeline function."""
    result = run_pipeline()
    assert result is None


def test_execute() -> None:
    """Test execute function."""
    result = execute()
    assert result is None


def test_main() -> None:
    """Test main function."""
    result = main()
    assert result is None
