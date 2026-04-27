from dataclasses import asdict, dataclass
from pathlib import Path

import tomli_w


@dataclass()
class PlatformConfig:
    platform_name: str
    emulator_name: str
    path_to_emulator: str


class PlatformConfigWriter:
    CONFIG_PATH = Path.home().joinpath(".config/decksmith/platforms")
    TOML_FILE_EXTENSION = ".toml"

    def __call__(self, platform_config: PlatformConfig) -> None:
        platform_config_file_name = platform_config.emulator_name.lower().replace(
            " ", "_"
        )
        platform_config_path = self.CONFIG_PATH.joinpath(
            f"{platform_config_file_name}{self.TOML_FILE_EXTENSION}"
        )
        platform_config_path.parent.mkdir(exist_ok=True, parents=True)

        with open(platform_config_path, "wb") as file:
            tomli_w.dump(asdict(platform_config), file)
