from dataclasses import dataclass
from typing import Any


@dataclass
class HelloHelper:
    data: dict
    name: str = ''
    message: str = ''

    def __post_init__(self) -> None:
        self._set_data()

    def _set_data(self) -> None:
        self.name = self.data.get('name')
        self.message = self.data.get('message')