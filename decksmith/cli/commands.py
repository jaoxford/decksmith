import click

from ..config import GameConfig, GameConfigWriter, PlatformConfig, PlatformConfigWriter


@click.group()
def cli() -> None:
    pass


@cli.command()
@click.option("--name", "game_name", prompt="Name of Game")
@click.option("--platform", "platform_name", prompt="Name of Platform")
@click.option("--rom", "path_to_rom", prompt="Path to ROM")
@click.option("--profile", "profile_name", prompt="Name of Profile")
def create_game_config(
    game_name: str, platform_name: str, path_to_rom: str, profile_name: str
) -> None:
    """Create a new game config."""
    GameConfigWriter().write_game_config(
        GameConfig(
            game_name=game_name,
            platform_name=platform_name,
            path_to_rom=path_to_rom,
            profile_name=profile_name,
        )
    )


@cli.command()
@click.option("--platform-name", "platform_name", prompt="Name of Platform")
@click.option("--emulator-name", "emulator_name", prompt="Name of Emulator")
@click.option("--path-to-emulator", "path_to_emulator", prompt="Path to Emulator")
def create_platform_config(
    platform_name: str,
    emulator_name: str,
    path_to_emulator: str,
) -> None:
    """Create a new platform config."""
    PlatformConfigWriter()(
        PlatformConfig(
            platform_name=platform_name,
            emulator_name=emulator_name,
            path_to_emulator=path_to_emulator,
        )
    )
