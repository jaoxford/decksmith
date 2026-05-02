"""Tests for platform config writer."""

import tomllib

from decksmith.config.platform_config import PlatformConfig, PlatformConfigWriter


class TestPlatformConfigWriter:
    """Tests for platform config writer."""

    def test_writes_toml_file(
        self,
        tmp_path,
        monkeypatch,
    ) -> None:
        """Writer should create a TOML file with the correct content."""
        monkeypatch.setattr(PlatformConfigWriter, "CONFIG_PATH", tmp_path)
        config = PlatformConfig(
            platform_name="Steam",
        )

        PlatformConfigWriter()(config)

        expected_file = tmp_path / "steam.toml"
        assert expected_file.exists()
        with open(expected_file, "rb") as file:
            data = tomllib.load(file)
        assert data == {
            "emulator_name": "",
            "path_to_emulator": "",
            "platform_name": "Steam",
        }
