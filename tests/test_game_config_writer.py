"""Tests for game config writer."""

import tomllib

from decksmith.config.game_config import GameConfig, GameConfigWriter


class TestGameConfigWriter:
    """Tests for game config writer."""

    def test_writes_toml_file(
        self,
        tmp_path,
        monkeypatch,
    ) -> None:
        """Writer should create a TOML file with the correct content."""
        monkeypatch.setattr(GameConfigWriter, "CONFIG_PATH", tmp_path)
        config = GameConfig(
            game_name="Hollow Knight",
            platform_name="PC",
            path_to_rom="/games/hollow_knight.exe",
            profile_name="default",
            position_on_deck=1,
        )

        GameConfigWriter()(config)

        expected_file = tmp_path / "hollow_knight.toml"
        assert expected_file.exists()
        with open(expected_file, "rb") as file:
            data = tomllib.load(file)
        assert data == {
            "game_name": "Hollow Knight",
            "platform_name": "PC",
            "path_to_rom": "/games/hollow_knight.exe",
            "profile_name": "default",
            "position_on_deck": 1,
        }

    def test_filename_is_lowercased_and_underscored(
        self,
        tmp_path,
        monkeypatch,
    ) -> None:
        """Filename should be lowercased with spaces replaced by underscores."""
        monkeypatch.setattr(GameConfigWriter, "CONFIG_PATH", tmp_path)
        config = GameConfig(
            game_name="My Cool Game",
            platform_name="PC",
            path_to_rom="/games/my_cool_game.exe",
            profile_name="default",
        )

        GameConfigWriter()(config)

        assert (tmp_path / "my_cool_game.toml").exists()

    def test_position_on_deck_defaults_to_zero(
        self,
        tmp_path,
        monkeypatch,
    ) -> None:
        """position_on_deck should be written as 0 when not provided."""
        monkeypatch.setattr(GameConfigWriter, "CONFIG_PATH", tmp_path)
        config = GameConfig(
            game_name="Celeste",
            platform_name="PC",
            path_to_rom="/games/celeste.exe",
            profile_name="default",
        )

        GameConfigWriter()(config)

        with open(tmp_path / "celeste.toml", "rb") as file:
            data = tomllib.load(file)
        assert data["position_on_deck"] == 0
