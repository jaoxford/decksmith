"""Tests for toml reader."""

from pathlib import Path

import pytest

from decksmith.toml_reader import read_toml_file


class TestTomlReader:
    """Tests for toml reader."""

    def test_with_nonexistent_file(self) -> None:
        """Nonexistent file should raise an Exception"""
        with pytest.raises(FileNotFoundError):
            result = read_toml_file(
                Path(__file__).parent.joinpath("nonexistent_file.toml").as_posix()
            )

            assert not result

    def test_returns_expected_output_for_game(self) -> None:
        """Toml reader should return expected output for game."""
        expected = {
            "name": "Game Name",
            "platform": "Platform Name",
            "rom": "/path/to/rom",
            "profile": "Profile Name",
            "position": 1,
        }

        result = read_toml_file(
            Path(__file__).parent.joinpath("sample_game.toml").as_posix()
        )

        assert result == expected

    def test_returns_expected_output_for_platform(self) -> None:
        """Toml reader should return expected output for platform."""
        expected = {
            "name": "Platform Name",
            "emulator": "/path/to/platform",
        }

        result = read_toml_file(
            Path(__file__).parent.joinpath("sample_platform.toml").as_posix()
        )

        assert result == expected
