"""Library for reading toml files."""

import tomllib


def read_toml_file(file_path: str) -> dict:
    """Read from TOML file"""
    with open(file_path, "rb") as file:
        data = tomllib.load(file)

    return data
