from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Optional

import tomli_w


@dataclass()
class GameConfig:
    game_name: str
    platform_name: str
    path_to_rom: str
    profile_name: str
    position_on_deck: Optional[int] = None


class GameConfigWriter:
    CONFIG_PATH = Path.home().joinpath(".config/decksmith/games")
    TOML_FILE_EXTENSION = ".toml"

    def write_game_config(self, game_config: GameConfig) -> None:
        game_config_file_name = game_config.game_name.lower().replace(" ", "_")
        game_config_path = self.CONFIG_PATH.joinpath(
            f"{game_config_file_name}{self.TOML_FILE_EXTENSION}"
        )
        game_config_path.parent.mkdir(exist_ok=True, parents=True)

        if not game_config.position_on_deck:
            game_config.position_on_deck = 0

        with open(game_config_path, "wb") as file:
            tomli_w.dump(asdict(game_config), file)
