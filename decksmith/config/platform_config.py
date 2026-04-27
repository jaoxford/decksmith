from dataclasses import dataclass


@dataclass(frozen=True)
class PlatformConfig:
    name: str
    emulator: str
