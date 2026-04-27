import click

from decksmith.config.game_config import GameConfig

from ..config import GameConfigWriter


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
